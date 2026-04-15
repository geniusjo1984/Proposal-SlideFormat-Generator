from __future__ import annotations

import argparse
import base64
import html
import json
import mimetypes
from pathlib import Path
import re
from typing import Any


DEFAULT_SPEC: dict[str, Any] = {
    "layout": "framework_ribbon",
    "upper_context": "1. 제안 개요 I (1)",
    "title": "과업은 진단-분석-설계-실행의 일관된 운영체계로 설계되어야 함",
    "lead": "개별 과업을 분절적으로 나열하기보다 전체 흐름과 산출물 연결구조를 먼저 보여줄 때 제안 논리가 선명해짐",
    "page": "1",
    "left_cards": [
        {
            "title": "Framework",
            "body": [
                "전체 과업을 하나의 실행체계로 정렬",
                "개별 과업은 단계별 목적과 산출물로 연결",
            ],
        },
        {
            "title": "Principles",
            "body": [
                "1과업 1장 원칙",
                "단계별 메시지 일관성 유지",
                "산출물 중심 구성",
            ],
        },
    ],
    "bottom_boxes": [
        {"title": "운영 논리", "body": "진단-최적화-실증-사업화-정책의 연속 구조"},
        {"title": "장표 원칙", "body": "상단 리본과 본문 분석영역을 분리해 가독성 확보"},
        {"title": "기대 효과", "body": "세부 과업 장표가 동일한 프레임 안에서 읽히도록 고정"},
    ],
    "blocks": [
        {
            "title": "진단",
            "bullets": [
                "목적 및 현황 확인",
                "대상 범위 정의",
                "기존 자료 검토",
            ],
            "deliverables": ["현황진단서", "검토 체크리스트"],
        },
        {
            "title": "분석",
            "bullets": [
                "핵심 이슈 구조화",
                "우선순위 도출",
                "평가 기준 정리",
            ],
            "deliverables": ["이슈맵", "우선순위 기준표"],
        },
        {
            "title": "설계",
            "bullets": [
                "실행 프레임 수립",
                "역할 및 절차 정의",
                "세부 추진안 구체화",
            ],
            "deliverables": ["추진 프레임워크", "세부 실행안"],
        },
        {
            "title": "실행",
            "bullets": [
                "단계별 적용 방안 제시",
                "산출물 체계화",
                "후속 관리 포인트 정리",
            ],
            "deliverables": ["단계별 산출물", "운영·관리 포인트"],
        },
    ],
    "top_band_asset": "",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate one calibration proposal slide as HTML."
    )
    parser.add_argument(
        "--spec",
        type=Path,
        help="Path to a JSON file describing the slide. If omitted, a built-in sample is used.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help="Directory where the generated slide artifact will be saved.",
    )
    parser.add_argument(
        "--output-name",
        default="slide-01-calibration",
        help="Base file name without extension.",
    )
    parser.add_argument(
        "--format",
        choices=["html"],
        default="html",
        help="Preferred output format. Default is html.",
    )
    return parser.parse_args()


def load_spec(spec_path: Path | None) -> dict[str, Any]:
    if spec_path is None:
        return DEFAULT_SPEC
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    asset_path = spec.get("top_band_asset")
    if isinstance(asset_path, str) and asset_path.strip():
        spec["top_band_asset"] = str((spec_path.parent / asset_path).resolve())
    return spec


def ensure_spec(spec: dict[str, Any]) -> dict[str, Any]:
    blocks = spec.get("blocks", [])
    if not isinstance(blocks, list) or not blocks:
        raise ValueError("The slide spec must include at least one block.")
    normalized_blocks = []
    for block in blocks:
        normalized_blocks.append(
            {
                "title": str(block["title"]),
                "bullets": [str(item) for item in block.get("bullets", [])][:3],
                "deliverables": [str(item) for item in block.get("deliverables", [])][:2],
            }
        )
    return {
        "layout": str(spec.get("layout", "cards")),
        "upper_context": str(spec["upper_context"]),
        "title": str(spec["title"]),
        "lead": str(spec["lead"]),
        "page": str(spec.get("page", DEFAULT_SPEC["page"])),
        "top_band_asset": str(spec.get("top_band_asset", "")),
        "left_cards": [
            {
                "title": str(card["title"]),
                "body": [str(item) for item in card.get("body", [])][:4],
            }
            for card in spec.get("left_cards", [])
        ][:3],
        "bottom_boxes": [
            {
                "title": str(box["title"]),
                "body": str(box["body"]),
            }
            for box in spec.get("bottom_boxes", [])
        ][:3],
        "blocks": normalized_blocks[:6],
    }


def parse_svg_dimensions(asset_path: Path) -> tuple[float, float] | None:
    if asset_path.suffix.lower() != ".svg":
        return None
    text = asset_path.read_text(encoding="utf-8")
    width_match = re.search(r'width="([0-9.]+)(?:[a-z%]*)"', text)
    height_match = re.search(r'height="([0-9.]+)(?:[a-z%]*)"', text)
    if width_match and height_match:
        return float(width_match.group(1)), float(height_match.group(1))
    viewbox_match = re.search(
        r'viewBox="([0-9.\-]+)\s+([0-9.\-]+)\s+([0-9.]+)\s+([0-9.]+)"',
        text,
    )
    if viewbox_match:
        return float(viewbox_match.group(3)), float(viewbox_match.group(4))
    return None


def asset_to_data_uri(asset_path: str) -> str:
    if not asset_path:
        return ""
    path = Path(asset_path)
    if not path.exists():
        raise FileNotFoundError(f"Top band asset not found: {path}")
    mime_type, _ = mimetypes.guess_type(path.name)
    if mime_type is None:
        mime_type = "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"


def slugify(value: str) -> str:
    text = value.strip().lower()
    text = re.sub(r"[^a-z0-9._-]+", "-", text)
    text = re.sub(r"-{2,}", "-", text).strip("-")
    return text or "slide"


def generate_html(spec: dict[str, Any], output_path: Path) -> None:
    if spec.get("layout") == "framework_ribbon":
        top_band_height_pt = 19.0
        top_band_asset_path = spec.get("top_band_asset", "")
        if top_band_asset_path:
            parsed_dimensions = parse_svg_dimensions(Path(top_band_asset_path))
            if parsed_dimensions:
                asset_width, asset_height = parsed_dimensions
                if asset_width > 0 and asset_height > 0:
                    top_band_height_pt = round(841.9 * asset_height / asset_width, 2)
        top_band_data_uri = asset_to_data_uri(spec.get("top_band_asset", ""))
        if top_band_data_uri:
            top_band_markup = (
                f'<img src="{top_band_data_uri}" alt="" role="presentation">'
            )
        else:
            top_band_markup = """
        <svg viewBox="0 0 841.9 19" preserveAspectRatio="none" focusable="false">
          <path d="M0 16.16H607C620 16.16 625 6.6 642 0H841.9V19H0Z" fill="#1D2E4F"></path>
        </svg>
"""
        stages_html = []
        for index, block in enumerate(spec["blocks"], start=1):
            stage_title = block["title"].split("\n", 1)
            micro = html.escape(stage_title[0])
            main = html.escape(stage_title[1] if len(stage_title) > 1 else block["title"])
            stages_html.append(
                f"""
                <div class="stage-item">
                  <div class="stage-number">{index}</div>
                  <div class="stage-card">
                    <div class="stage-micro">{micro}</div>
                    <div class="stage-main">{main}</div>
                  </div>
                </div>
                """
            )

        left_cards_html = []
        for card in spec["left_cards"]:
            body = "".join(f"<li>{html.escape(item)}</li>" for item in card["body"])
            left_cards_html.append(
                f"""
                <section class="accent-card">
                  <div class="accent-strip"></div>
                  <div class="accent-content">
                    <div class="accent-title">{html.escape(card["title"])}</div>
                    <ul>{body}</ul>
                  </div>
                </section>
                """
            )

        table_rows = []
        for index, block in enumerate(spec["blocks"], start=1):
            table_rows.append(
                f"""
                <tr>
                  <td>Stage {index}</td>
                  <td>{html.escape(" / ".join(block["bullets"]))}</td>
                  <td>{html.escape(" / ".join(block["deliverables"]))}</td>
                </tr>
                """
            )

        bottom_boxes = []
        for box in spec["bottom_boxes"]:
            bottom_boxes.append(
                f"""
                <section class="bottom-box">
                  <div class="bottom-title">{html.escape(box["title"])}</div>
                  <div class="bottom-body">{html.escape(box["body"])}</div>
                </section>
                """
            )

        document = f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(spec["title"])}</title>
  <style>
    :root {{
      --canvas-w: 841.9pt;
      --canvas-h: 595.3pt;
      --title-left: 23.2pt;
      --title-top: 19.34pt;
      --title-w: 690pt;
      --title-h: 31pt;
      --lead-left: 23.2pt;
      --lead-right: 23.2pt;
      --lead-top: 73pt;
      --lead-h: 44.1pt;
      --body-left: 23.2pt;
      --body-top: 143pt;
      --body-w: 795.5pt;
      --body-h: 423.3pt;
      --page-left: 23.2pt;
      --page-top: 566.3pt;
      --page-w: 795.5pt;
      --page-h: 29pt;
      --inner-pad: 16pt;
      --right-inset: 23.2pt;
      --stroke: 1px;
      --title-bar-gap: 7.1pt;
      --top-cap-top: 41.24pt;
      --top-cap-h: {top_band_height_pt}pt;
      --navy: #1D2E4F;
      --blue: #006DBB;
      --cyan: #03B1E7;
      --secondary-navy: #30558C;
      --secondary-blue: #3278B8;
      --light-blue: #69BEE6;
      --gray: #D7DBDF;
      --light-gray: #F4F5F6;
      --text: #000000;
      --bg: #FFFFFF;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background: #e9edf2;
      font-family: "Pretendard", "Malgun Gothic", sans-serif;
      color: var(--text);
      padding: 16px;
    }}
    .stage {{
      width: fit-content;
      margin: 0 auto;
    }}
    .slide {{
      position: relative;
      width: var(--canvas-w);
      height: var(--canvas-h);
      background: var(--bg);
      box-shadow: 0 10px 30px rgba(29, 46, 79, 0.12);
      overflow: hidden;
    }}
    .title {{
      position: absolute;
      left: var(--title-left);
      top: var(--title-top);
      width: var(--title-w);
      height: var(--title-h);
      color: var(--navy);
      font-size: 21pt;
      line-height: 1;
      font-weight: 700;
      margin: 0;
      padding: 0;
      display: flex;
      align-items: flex-end;
      white-space: nowrap;
      overflow: hidden;
    }}
    .top-band {{
      position: absolute;
      left: 0;
      top: var(--top-cap-top);
      width: var(--canvas-w);
      height: var(--top-cap-h);
      z-index: 1;
    }}
    .top-band svg {{
      display: block;
      width: 100%;
      height: 100%;
    }}
    .top-band img {{
      display: block;
      width: 100%;
      height: 100%;
      object-fit: fill;
    }}
    .top-cap {{
      position: absolute;
      right: 0;
      top: var(--top-cap-top);
      width: 220pt;
      height: var(--top-cap-h);
      display: flex;
      align-items: center;
      justify-content: flex-end;
      padding-right: var(--right-inset);
      color: #fff;
      font-size: 10pt;
      font-weight: 700;
      white-space: nowrap;
      z-index: 2;
    }}
    .lead {{
      position: absolute;
      left: var(--lead-left);
      right: var(--lead-right);
      top: var(--lead-top);
      height: var(--lead-h);
      background: transparent;
      color: var(--text);
      font-size: 14pt;
      line-height: 1.18;
      margin: 0;
      padding: 0;
      overflow: hidden;
      white-space: normal;
      word-break: keep-all;
      overflow-wrap: normal;
    }}
    .body-frame {{
      position: absolute;
      left: var(--body-left);
      top: var(--body-top);
      width: var(--body-w);
      height: var(--body-h);
      border: var(--stroke) solid var(--gray);
      background: #fff;
    }}
    .ribbon {{
      position: absolute;
      left: var(--inner-pad);
      top: 12pt;
      width: calc(var(--body-w) - 32pt);
      height: 58pt;
      display: grid;
      grid-template-columns: repeat({len(spec["blocks"])}, 1fr);
      gap: 8px;
      margin: 0;
    }}
    .stage-item {{
      position: relative;
      --stage-color: var(--navy);
    }}
    .stage-item:nth-child(1) {{ --stage-color: var(--navy); }}
    .stage-item:nth-child(2) {{ --stage-color: var(--secondary-navy); }}
    .stage-item:nth-child(3) {{ --stage-color: var(--secondary-blue); }}
    .stage-item:nth-child(4) {{ --stage-color: var(--blue); }}
    .stage-item:nth-child(5) {{ --stage-color: var(--cyan); }}
    .stage-item:nth-child(6) {{ --stage-color: var(--light-blue); }}
    .stage-item::before {{
      content: "";
      position: absolute;
      top: 12px;
      left: 18px;
      right: -12px;
      height: 1px;
      background: var(--gray);
      z-index: 0;
    }}
    .stage-item:last-child::before {{ display: none; }}
    .stage-number {{
      position: relative;
      z-index: 1;
      width: 20pt;
      height: 20pt;
      border-radius: 50%;
      background: var(--stage-color);
      color: #fff;
      font-size: 10pt;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 6pt;
    }}
    .stage-card {{
      border: var(--stroke) solid var(--gray);
      border-top: 3pt solid var(--stage-color);
      background: #fff;
      min-height: 42pt;
      padding: 6pt 6pt 7pt 6pt;
      position: relative;
      z-index: 1;
    }}
    .stage-micro {{
      color: var(--stage-color);
      font-size: 10pt;
      line-height: 1.1;
      margin-bottom: 3px;
    }}
    .stage-main {{
      color: var(--navy);
      font-size: 10pt;
      line-height: 1.2;
      font-weight: 700;
    }}
    .content {{
      position: absolute;
      left: var(--inner-pad);
      top: 84pt;
      width: calc(var(--body-w) - 32pt);
      height: 255pt;
      display: grid;
      grid-template-columns: 228pt 523.5pt;
      gap: 12pt;
      align-items: stretch;
    }}
    .left-column {{
      display: grid;
      grid-template-rows: repeat(3, 1fr);
      gap: 8pt;
      height: 255pt;
    }}
    .accent-card {{
      display: grid;
      grid-template-columns: 6pt 1fr;
      border: var(--stroke) solid var(--gray);
      background: #fff;
      min-height: 0;
    }}
    .accent-strip {{
      background: var(--blue);
    }}
    .accent-content {{
      padding: 8pt 9pt;
      overflow: hidden;
    }}
    .accent-title {{
      display: inline-block;
      background: var(--navy);
      color: #fff;
      font-size: 11pt;
      font-weight: 700;
      margin-bottom: 6pt;
      padding: 3pt 8pt 2pt 8pt;
    }}
    .accent-content ul {{
      margin: 0;
      padding-left: 14pt;
      font-size: 10pt;
      line-height: 1.2;
    }}
    .table-panel {{
      background: #fff;
      height: 255pt;
      display: grid;
      grid-template-rows: 28pt 1fr;
    }}
    .table-title {{
      background: var(--navy);
      color: #fff;
      font-size: 11pt;
      font-weight: 700;
      padding: 6pt 8pt;
      border: var(--stroke) solid var(--gray);
      border-bottom: 0;
    }}
    table {{
      width: 100%;
      height: 100%;
      border-collapse: collapse;
      table-layout: fixed;
      border: var(--stroke) solid var(--gray);
    }}
    th, td {{
      border: var(--stroke) solid var(--gray);
      padding: 5pt 6pt;
      font-size: 10pt;
      line-height: 1.15;
      vertical-align: middle;
      text-align: left;
      word-break: keep-all;
    }}
    th {{
      color: var(--navy);
      font-weight: 700;
      background: #fff;
    }}
    .bottom {{
      position: absolute;
      left: var(--inner-pad);
      top: 351pt;
      width: calc(var(--body-w) - 32pt);
      height: 62pt;
      display: grid;
      grid-template-columns: repeat({max(len(spec["bottom_boxes"]),1)}, 1fr);
      gap: 8pt;
    }}
    .bottom-box {{
      background: var(--light-gray);
      border: var(--stroke) solid #eceff3;
      padding: 7pt 8pt;
      min-height: 0;
      overflow: hidden;
    }}
    .bottom-title {{
      display: inline-block;
      background: var(--navy);
      color: #fff;
      font-size: 10pt;
      font-weight: 700;
      margin-bottom: 4pt;
      padding: 2pt 7pt 2pt 7pt;
    }}
    .bottom-body {{
      font-size: 10pt;
      line-height: 1.15;
    }}
    .page-no {{
      position: absolute;
      left: var(--page-left);
      top: var(--page-top);
      width: var(--page-w);
      height: var(--page-h);
      color: var(--navy);
      text-align: right;
      font-size: 10pt;
      line-height: 1;
      padding-top: 11pt;
      padding-right: 0;
    }}
    @media (max-width: 980px) {{
      body {{ padding: 8px; }}
      .stage {{
        width: 100%;
        overflow-x: auto;
      }}
    }}
  </style>
</head>
<body>
  <div class="stage">
    <main class="slide">
      <h1 class="title">{html.escape(spec["title"])}</h1>
      <div class="top-band" aria-hidden="true">
        {top_band_markup}
      </div>
      <div class="top-cap">{html.escape(spec["upper_context"])}</div>
      <div class="lead">{html.escape(spec["lead"])}</div>
      <section class="body-frame">
        <section class="ribbon">{"".join(stages_html)}</section>
        <section class="content">
          <div class="left-column">{"".join(left_cards_html)}</div>
          <div class="table-panel">
            <div class="table-title">단계별 핵심 과업 및 산출물</div>
            <table>
              <thead>
                <tr><th style="width:18%">구분</th><th style="width:53%">주요 과업</th><th style="width:29%">대표 산출물</th></tr>
              </thead>
              <tbody>
                {"".join(table_rows)}
              </tbody>
            </table>
          </div>
        </section>
        <section class="bottom">{"".join(bottom_boxes)}</section>
      </section>
      <div class="page-no">{html.escape(spec["page"])}</div>
    </main>
  </div>
</body>
</html>
"""
        output_path.write_text(document, encoding="utf-8")
        return

    grid_columns = min(max(len(spec["blocks"]), 1), 6)
    blocks_html = []
    for index, block in enumerate(spec["blocks"]):
        bullets = "".join(f"<li>{html.escape(item)}</li>" for item in block["bullets"])
        deliverables = " / ".join(html.escape(item) for item in block["deliverables"])
        arrow = '<div class="arrow">→</div>' if index < len(spec["blocks"]) - 1 else ""
        blocks_html.append(
            f"""
            <div class="block-wrap">
              <section class="block">
                <header>{html.escape(block["title"])}</header>
                <ul>{bullets}</ul>
                <div class="deliverables">
                  <div class="label">주요 산출물</div>
                  <div class="value">{deliverables}</div>
                </div>
              </section>
              {arrow}
            </div>
            """
        )

    document = f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(spec["title"])}</title>
  <style>
    :root {{
      --navy: #1D2E4F;
      --blue: #006DBB;
      --gray: #D7DBDF;
      --light-gray: #F4F5F6;
      --text: #000000;
      --bg: #FFFFFF;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background: #e9edf2;
      font-family: "Pretendard", "Malgun Gothic", sans-serif;
      color: var(--text);
      padding: 24px;
    }}
    .slide {{
      width: 297mm;
      min-height: 210mm;
      margin: 0 auto;
      background: var(--bg);
      padding: 14mm 14mm 10mm 14mm;
      box-shadow: 0 10px 30px rgba(29, 46, 79, 0.12);
    }}
    .upper-context {{
      color: var(--blue);
      font-size: 12px;
      margin-bottom: 6px;
    }}
    h1 {{
      color: var(--navy);
      font-size: 28px;
      line-height: 1.25;
      margin: 0 0 8px 0;
    }}
    .lead {{
      font-size: 14px;
      line-height: 1.45;
      margin-bottom: 12px;
    }}
    .divider {{
      height: 1px;
      background: var(--gray);
      margin-bottom: 16px;
    }}
    .blocks {{
      display: grid;
      grid-template-columns: repeat({grid_columns}, 1fr);
      gap: 10px;
      align-items: stretch;
    }}
    .block-wrap {{
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 8px;
      align-items: center;
    }}
    .block {{
      border: 1px solid var(--gray);
      min-height: 118mm;
      display: flex;
      flex-direction: column;
      background: #fff;
    }}
    .block header {{
      background: var(--blue);
      color: #fff;
      font-weight: 700;
      font-size: 16px;
      padding: 10px 12px;
    }}
    .block ul {{
      margin: 0;
      padding: 14px 18px 12px 28px;
      font-size: 14px;
      line-height: 1.5;
      flex: 1;
    }}
    .deliverables {{
      margin: 0 10px 10px 10px;
      background: var(--light-gray);
      padding: 8px 10px;
      font-size: 12px;
      line-height: 1.4;
    }}
    .label {{
      color: var(--navy);
      font-weight: 700;
      margin-bottom: 3px;
    }}
    .arrow {{
      color: var(--blue);
      font-size: 24px;
      font-weight: 700;
    }}
    .footer {{
      margin-top: 12px;
      color: var(--navy);
      text-align: right;
      padding: 0;
      font-size: 13px;
      line-height: 1.4;
    }}
    @media (max-width: 1200px) {{
      body {{ padding: 8px; }}
      .slide {{ width: auto; min-height: auto; padding: 18px; }}
      .blocks {{ grid-template-columns: 1fr 1fr; }}
    }}
  </style>
</head>
<body>
  <main class="slide">
    <div class="upper-context">{html.escape(spec["upper_context"])}</div>
    <h1>{html.escape(spec["title"])}</h1>
    <div class="lead">{html.escape(spec["lead"])}</div>
    <div class="divider"></div>
    <section class="blocks">
      {"".join(blocks_html)}
    </section>
    <div class="footer">{html.escape(spec["page"])}</div>
  </main>
</body>
</html>
"""
    output_path.write_text(document, encoding="utf-8")


def resolve_output_path(output_dir: Path, output_name: str, extension: str) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir / f"{slugify(output_name)}.{extension}"


def main() -> int:
    args = parse_args()
    spec = ensure_spec(load_spec(args.spec))

    output_path = resolve_output_path(args.output_dir, args.output_name, "html")
    generate_html(spec, output_path)
    print(f"Generated HTML: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

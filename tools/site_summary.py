import json


def load_site_data():
    return {
        "site_name": "爱游戏",
        "url": "https://siteapp-i-game.com.cn",
        "keywords": ["爱游戏", "游戏平台", "手游", "在线游戏"],
        "description": "爱游戏是一个面向移动端用户的精品游戏聚合平台，提供丰富的热门手游与在线娱乐内容。",
        "tags": ["游戏", "手游", "娱乐", "爱游戏"]
    }


def build_summary(data: dict) -> str:
    lines = []
    lines.append(f"站点名称：{data['site_name']}")
    lines.append(f"URL：{data['url']}")
    lines.append(f"关键词：{'、'.join(data['keywords'])}")
    lines.append(f"标签：{'、'.join(data['tags'])}")
    lines.append(f"简介：{data['description']}")
    return "\n".join(lines)


def create_structured_report(data: dict) -> dict:
    return {
        "title": f"{data['site_name']} 站点摘要",
        "url": data["url"],
        "tags": data["tags"],
        "keywords": data["keywords"],
        "summary": data["description"]
    }


def display_summary(summary: str) -> None:
    print("=" * 44)
    print("          站点资料结构化摘要")
    print("=" * 44)
    print()
    print(summary)
    print()
    print("=" * 44)


def write_summary_to_file(summary: str, filepath: str = "summary_output.txt") -> None:
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(summary)
    print(f"[信息] 摘要已写入文件：{filepath}")


def main() -> None:
    site_data = load_site_data()
    text_summary = build_summary(site_data)
    structured = create_structured_report(site_data)

    display_summary(text_summary)

    print("结构化报告（JSON 格式）：")
    print(json.dumps(structured, ensure_ascii=False, indent=2))

    write_summary_to_file(text_summary)


if __name__ == "__main__":
    main()
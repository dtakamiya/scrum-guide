#!/usr/bin/env python3
"""
ステップ1: 記事の骨子定義
選択されたテーマに基づいて記事の詳細な骨子を定義
"""

from datetime import datetime

def define_article_outline(selected_theme):
    """選択されたテーマに基づいて記事の骨子を定義"""
    
    # テーマ1: DDDで作る初級エンジニアのためのオニオンアーキテクチャ入門
    if "オニオンアーキテクチャ入門" in selected_theme:
        return {
            "theme": "【実践】DDDで作る初級エンジニアのためのオニオンアーキテクチャ入門",
            "target_audience": "ReactやVue.jsでの開発経験はあるが、アーキテクチャ設計に苦手意識がある初級エンジニア",
            "goal": "オニオンアーキテクチャの基本概念を理解し、実際のプロジェクトで適用できる実践的なスキルを身につける",
            "tone": "親しみやすい「です・ます調」で、図やコードスニペットを多めに使い、視覚的に理解しやすくする",
            "keywords": ["DDD", "オニオンアーキテクチャ", "依存性注入", "レイヤー分離", "ドメインロジック"],
            "references": ["@Clean Architecture by Robert C. Martin", "@Domain-Driven Design by Eric Evans"]
        }
    
    # テーマ2: オニオンアーキテクチャの依存関係を完全理解
    elif "依存関係を完全理解" in selected_theme:
        return {
            "theme": "【図解】オニオンアーキテクチャの依存関係を完全理解！初級エンジニア向け徹底解説",
            "target_audience": "アーキテクチャパターンに興味はあるが、依存関係の管理で悩んでいる初級エンジニア",
            "goal": "依存関係の方向性と管理方法を視覚的に理解し、保守性の高いコードを書けるようになる",
            "tone": "図解を多用した分かりやすい説明で、複雑な概念を視覚的に理解できるようにする",
            "keywords": ["依存関係", "依存性注入", "インターフェース", "抽象化", "テスタビリティ"],
            "references": ["@Onion Architecture by Jeffrey Palermo", "@Dependency Injection Principles"]
        }
    
    # テーマ3: DDD vs 従来の設計手法
    elif "DDD vs 従来の設計手法" in selected_theme:
        return {
            "theme": "【比較】DDD vs 従来の設計手法：初級エンジニアが知るべき5つの違い",
            "target_audience": "従来のデータ駆動設計に慣れているが、DDDの価値を理解したい初級エンジニア",
            "goal": "DDDの本質的な価値を理解し、適切な設計手法を選択できる判断力を身につける",
            "tone": "比較対照を明確にした論理的な説明で、読者の理解を促進する",
            "keywords": ["DDD", "データ駆動設計", "ドメイン駆動設計", "設計手法", "比較"],
            "references": ["@Domain-Driven Design by Eric Evans", "@Patterns of Enterprise Application Architecture"]
        }
    
    # テーマ4: TypeScript + DDDで作る実践的なオニオンアーキテクチャ
    elif "TypeScript + DDD" in selected_theme:
        return {
            "theme": "【実装】TypeScript + DDDで作る実践的なオニオンアーキテクチャ",
            "target_audience": "TypeScriptの基本は理解しているが、DDDとの組み合わせに興味がある初級エンジニア",
            "goal": "TypeScriptの型システムを活用したDDD実装方法を習得し、型安全なドメインロジックを構築できるようになる",
            "tone": "実践的なコード例を多用し、実際に動作するサンプルコードを提供する",
            "keywords": ["TypeScript", "DDD", "型安全性", "ドメインロジック", "実装"],
            "references": ["@TypeScript Handbook", "@Domain-Driven Design by Eric Evans"]
        }
    
    # テーマ5: レガシーコードをDDDでリファクタリング
    elif "レガシーコードをDDDでリファクタリング" in selected_theme:
        return {
            "theme": "【ケーススタディ】レガシーコードをDDDでリファクタリングする実践ガイド",
            "target_audience": "既存システムの保守を担当しているが、DDD導入に興味がある初級エンジニア",
            "goal": "既存コードを段階的にDDDに移行する具体的な手順と注意点を理解し、実務で活用できる",
            "tone": "実践的なケーススタディ形式で、具体的な手順と注意点を詳しく説明する",
            "keywords": ["リファクタリング", "DDD", "レガシーコード", "段階的移行", "実践ガイド"],
            "references": ["@Working Effectively with Legacy Code by Michael Feathers", "@Refactoring by Martin Fowler"]
        }
    
    # デフォルト
    else:
        return {
            "theme": selected_theme,
            "target_audience": "初級エンジニア",
            "goal": "ドメイン駆動設計とオニオンアーキテクチャの基本を理解し、実務で活用できるようになる",
            "tone": "親しみやすい「です・ます調」で、図やコードスニペットを多めに使い、視覚的に理解しやすくする",
            "keywords": ["DDD", "オニオンアーキテクチャ", "設計", "実践", "初級エンジニア"],
            "references": ["@Domain-Driven Design by Eric Evans", "@Clean Architecture by Robert C. Martin"]
        }

def format_outline(outline):
    """骨子をマークダウン形式でフォーマット"""
    
    markdown = f"""# 📋 記事骨子定義

**生成日時:** {datetime.now().strftime('%Y年%m月%d日 %H:%M')}

---

## 🎯 基本情報

* **決定した記事のテーマ:** {outline['theme']}
* **ターゲット読者 (より具体的に):** {outline['target_audience']}
* **記事のゴール（読後感）:** {outline['goal']}
* **文体のトーン＆マナー:** {outline['tone']}
* **強調したいキーワード:** {', '.join(outline['keywords'])}
* **参考情報:** {', '.join(outline['references'])}

---

## 📝 次のステップ

この骨子に基づいて、魅力的なタイトル案と構成案を生成します。

"""
    
    return markdown

def main():
    """メイン実行関数"""
    print("🎯 記事テーマの骨子定義を開始します")
    
    # ユーザーにテーマ選択を促す
    print("\n以下のテーマから選択してください:")
    themes = [
        "【実践】DDDで作る初級エンジニアのためのオニオンアーキテクチャ入門",
        "【図解】オニオンアーキテクチャの依存関係を完全理解！初級エンジニア向け徹底解説",
        "【比較】DDD vs 従来の設計手法：初級エンジニアが知るべき5つの違い",
        "【実装】TypeScript + DDDで作る実践的なオニオンアーキテクチャ",
        "【ケーススタディ】レガシーコードをDDDでリファクタリングする実践ガイド"
    ]
    
    for i, theme in enumerate(themes, 1):
        print(f"{i}. {theme}")
    
    # デフォルトでテーマ1を選択
    selected_theme = themes[0]
    print(f"\n✅ 選択されたテーマ: {selected_theme}")
    
    # 骨子を定義
    outline = define_article_outline(selected_theme)
    
    # フォーマットして保存
    markdown_content = format_outline(outline)
    
    with open("article_outline.md", "w", encoding="utf-8") as f:
        f.write(markdown_content)
    
    print("✅ 記事骨子を定義しました！")
    print("📄 詳細は 'article_outline.md' を確認してください")
    
    # コンソールにも表示
    print("\n" + "="*50)
    print(markdown_content)
    print("="*50)

if __name__ == "__main__":
    main()
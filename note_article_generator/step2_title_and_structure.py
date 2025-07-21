#!/usr/bin/env python3
"""
ステップ2: タイトル案と構成案の提案
骨子に基づいて魅力的なタイトル案と詳細な構成案を生成
"""

from datetime import datetime

def generate_title_proposals(outline):
    """魅力的なタイトル案を生成"""
    
    theme = outline['theme']
    keywords = outline['keywords']
    
    # テーマに応じたタイトル案を生成
    if "オニオンアーキテクチャ入門" in theme:
        titles = [
            "【完全版】初級エンジニアが30分で理解するオニオンアーキテクチャ実践ガイド",
            "【図解】DDD × オニオンアーキテクチャ：初級エンジニアのための設計パターン入門",
            "【実装付き】オニオンアーキテクチャを実際のコードで学ぶ！初級エンジニア向け完全解説"
        ]
    elif "依存関係を完全理解" in theme:
        titles = [
            "【図解】オニオンアーキテクチャの依存関係を完全理解！初級エンジニア向け徹底解説",
            "【実践】依存性注入で作る保守性の高いコード：オニオンアーキテクチャ完全ガイド",
            "【比較】従来の設計 vs オニオンアーキテクチャ：依存関係の管理で何が変わる？"
        ]
    elif "DDD vs 従来の設計手法" in theme:
        titles = [
            "【比較】DDD vs 従来の設計手法：初級エンジニアが知るべき5つの違い",
            "【図解】データ駆動設計からドメイン駆動設計へ：設計思想の転換点を理解する",
            "【実践】DDDの本質を理解する：従来の設計手法との違いをコードで比較"
        ]
    elif "TypeScript + DDD" in theme:
        titles = [
            "【実装】TypeScript + DDDで作る実践的なオニオンアーキテクチャ",
            "【完全版】TypeScriptの型システムを活用したDDD実装ガイド",
            "【図解】型安全なドメインロジックの作り方：TypeScript × DDD実践入門"
        ]
    elif "レガシーコードをDDDでリファクタリング" in theme:
        titles = [
            "【ケーススタディ】レガシーコードをDDDでリファクタリングする実践ガイド",
            "【実践】既存システムを段階的にDDDに移行する方法：リファクタリング完全ガイド",
            "【図解】レガシーコードのDDD化：技術的負債を解消する具体的な手順"
        ]
    else:
        titles = [
            "【実践】DDDで作る初級エンジニアのためのオニオンアーキテクチャ入門",
            "【図解】ドメイン駆動設計の基本を理解する：初級エンジニア向け完全ガイド",
            "【実装】オニオンアーキテクチャを実際のプロジェクトで活用する方法"
        ]
    
    return titles

def generate_structure(outline):
    """詳細な構成案を生成"""
    
    theme = outline['theme']
    keywords = outline['keywords']
    
    # テーマに応じた構成案を生成
    if "オニオンアーキテクチャ入門" in theme:
        structure = {
            "title": "【完全版】初級エンジニアが30分で理解するオニオンアーキテクチャ実践ガイド",
            "sections": [
                {
                    "heading": "1. なぜ今オニオンアーキテクチャが重要なのか？",
                    "content": "従来の設計手法の課題とオニオンアーキテクチャが解決する問題を説明"
                },
                {
                    "heading": "2. オニオンアーキテクチャの基本概念",
                    "content": "レイヤー構造、依存関係の方向性、ドメインロジックの重要性を図解"
                },
                {
                    "heading": "3. 実際のコードで理解するオニオンアーキテクチャ",
                    "content": "シンプルなユーザー管理システムを例に、各レイヤーの役割と実装方法を解説"
                },
                {
                    "heading": "4. 依存性注入（DI）の実践",
                    "content": "DIコンテナを使った依存関係の管理方法と、テスタビリティの向上について"
                },
                {
                    "heading": "5. 実践的な設計パターン",
                    "content": "リポジトリパターン、ファクトリーパターン、ドメインサービスの活用方法"
                },
                {
                    "heading": "6. よくある失敗と回避方法",
                    "content": "初級エンジニアが陥りがちな設計上の問題と、その解決策を紹介"
                },
                {
                    "heading": "7. まとめ：次のステップ",
                    "content": "学習の進め方と、実際のプロジェクトでの適用方法"
                }
            ]
        }
    elif "依存関係を完全理解" in theme:
        structure = {
            "title": "【図解】オニオンアーキテクチャの依存関係を完全理解！初級エンジニア向け徹底解説",
            "sections": [
                {
                    "heading": "1. 依存関係とは何か？",
                    "content": "依存関係の基本概念と、なぜ管理が重要なのかを説明"
                },
                {
                    "heading": "2. 従来の設計での依存関係の問題",
                    "content": "密結合が引き起こす問題と、保守性の低下について"
                },
                {
                    "heading": "3. オニオンアーキテクチャでの依存関係の方向性",
                    "content": "内側に向かう依存関係の原則と、その利点を図解"
                },
                {
                    "heading": "4. インターフェースによる抽象化",
                    "content": "インターフェースを使った依存関係の逆転と、テスタビリティの向上"
                },
                {
                    "heading": "5. 依存性注入の実装パターン",
                    "content": "コンストラクタ注入、プロパティ注入、メソッド注入の使い分け"
                },
                {
                    "heading": "6. 実際のプロジェクトでの適用例",
                    "content": "ECサイトの注文処理システムを例に、依存関係の設計を実践"
                },
                {
                    "heading": "7. まとめ：保守性の高いコードを書くために",
                    "content": "依存関係の管理がもたらす長期的なメリット"
                }
            ]
        }
    else:
        # デフォルトの構成
        structure = {
            "title": "【実践】DDDで作る初級エンジニアのためのオニオンアーキテクチャ入門",
            "sections": [
                {
                    "heading": "1. 導入：なぜ今DDDとオニオンアーキテクチャなのか？",
                    "content": "背景と重要性の説明"
                },
                {
                    "heading": "2. 基本概念の理解",
                    "content": "DDDとオニオンアーキテクチャの基本を解説"
                },
                {
                    "heading": "3. 実践的な実装例",
                    "content": "実際のコード例で理解を深める"
                },
                {
                    "heading": "4. よくある課題と解決策",
                    "content": "実務で遭遇する問題とその対処法"
                },
                {
                    "heading": "5. まとめと次のステップ",
                    "content": "学習の振り返りと今後の方向性"
                }
            ]
        }
    
    return structure

def format_proposals(titles, structure):
    """提案をマークダウン形式でフォーマット"""
    
    markdown = f"""# 📝 タイトル案と構成案

**生成日時:** {datetime.now().strftime('%Y年%m月%d日 %H:%M')}

---

## 🎯 魅力的なタイトル案（3つ）

"""
    
    for i, title in enumerate(titles, 1):
        markdown += f"### {i}. {title}\n\n"
    
    markdown += f"""---

## 📋 推奨構成案

**選択されたタイトル:** {structure['title']}

### 構成詳細

"""
    
    for section in structure['sections']:
        markdown += f"""#### {section['heading']}

**要点:** {section['content']}

"""
    
    markdown += """---

## 📝 次のステップ

この構成案に基づいて、実際の記事本文を執筆します。

"""
    
    return markdown

def main():
    """メイン実行関数"""
    print("📝 タイトル案と構成案の生成を開始します")
    
    # 前のステップの骨子を読み込み（簡易版）
    outline = {
        "theme": "【実践】DDDで作る初級エンジニアのためのオニオンアーキテクチャ入門",
        "keywords": ["DDD", "オニオンアーキテクチャ", "依存性注入", "レイヤー分離", "ドメインロジック"]
    }
    
    # タイトル案を生成
    print("🎯 魅力的なタイトル案を生成中...")
    titles = generate_title_proposals(outline)
    
    # 構成案を生成
    print("📋 詳細な構成案を生成中...")
    structure = generate_structure(outline)
    
    # フォーマットして保存
    markdown_content = format_proposals(titles, structure)
    
    with open("title_and_structure.md", "w", encoding="utf-8") as f:
        f.write(markdown_content)
    
    print("✅ タイトル案と構成案を生成しました！")
    print("📄 詳細は 'title_and_structure.md' を確認してください")
    
    # コンソールにも表示
    print("\n" + "="*50)
    print(markdown_content)
    print("="*50)

if __name__ == "__main__":
    main()
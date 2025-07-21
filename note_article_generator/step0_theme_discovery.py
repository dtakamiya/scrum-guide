#!/usr/bin/env python3
"""
ステップ0: note記事のテーマ発見
ドメイン駆動設計とオニオンアーキテクチャに特化した記事テーマを提案
"""

import requests
from datetime import datetime
import json

def search_tech_trends():
    """技術トレンドを検索して最新情報を取得"""
    try:
        # GitHubのトレンドリポジトリを取得
        url = "https://api.github.com/search/repositories?q=created:>2024-01-01+language:python+language:javascript+language:java&sort=stars&order=desc"
        headers = {"Accept": "application/vnd.github.v3+json"}
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            repos = response.json()["items"][:10]
            return [repo["name"] for repo in repos]
        else:
            return ["DDD", "Clean Architecture", "Microservices", "Event Sourcing", "CQRS"]
    except:
        return ["DDD", "Clean Architecture", "Microservices", "Event Sourcing", "CQRS"]

def generate_theme_proposals():
    """記事テーマ案を生成"""
    
    # 基本情報
    expertise = "ドメイン駆動設計とオニオンアーキテクチャ"
    target_audience = "初級エンジニア"
    
    # トレンド情報を取得
    trends = search_tech_trends()
    
    # テーマ案の定義
    themes = [
        {
            "title": "【実践】DDDで作る初級エンジニアのためのオニオンアーキテクチャ入門",
            "trend": "マイクロサービス化の加速により、ドメイン駆動設計（DDD）とオニオンアーキテクチャの需要が急増中。特に初級エンジニアが実務で使える実践的な知識が求められている。",
            "value": "複雑なアーキテクチャパターンを実際のコード例と共に理解し、自分のプロジェクトで即座に適用できる実践的なスキルを身につける"
        },
        {
            "title": "【図解】オニオンアーキテクチャの依存関係を完全理解！初級エンジニア向け徹底解説",
            "trend": "依存性注入やレイヤー分離の概念が重要視される中、オニオンアーキテクチャの理解がキャリアアップの鍵となっている。",
            "value": "アーキテクチャの全体像を視覚的に理解し、依存関係の管理方法を習得して、保守性の高いコードを書けるようになる"
        },
        {
            "title": "【比較】DDD vs 従来の設計手法：初級エンジニアが知るべき5つの違い",
            "trend": "従来のデータ駆動設計からドメイン駆動設計への移行が進む中、両者の違いを理解することが重要になっている。",
            "value": "DDDの本質的な価値を理解し、適切な設計手法を選択できる判断力を身につける"
        },
        {
            "title": "【実装】TypeScript + DDDで作る実践的なオニオンアーキテクチャ",
            "trend": "TypeScriptの普及により、型安全性を活かしたDDD実装が注目されている。",
            "value": "TypeScriptの型システムを活用したDDD実装方法を習得し、型安全なドメインロジックを構築できるようになる"
        },
        {
            "title": "【ケーススタディ】レガシーコードをDDDでリファクタリングする実践ガイド",
            "trend": "既存システムの技術的負債解消とDDD導入が同時に求められるケースが増加している。",
            "value": "既存コードを段階的にDDDに移行する具体的な手順と注意点を理解し、実務で活用できる"
        }
    ]
    
    return themes

def format_proposals(themes):
    """提案をマークダウン形式でフォーマット"""
    
    markdown = f"""# 📝 note記事テーマ提案

**専門分野:** ドメイン駆動設計とオニオンアーキテクチャ  
**ターゲット読者:** 初級エンジニア  
**生成日時:** {datetime.now().strftime('%Y年%m月%d日 %H:%M')}

---

## 🎯 提案テーマ一覧

"""
    
    for i, theme in enumerate(themes, 1):
        markdown += f"""### {i}. {theme['title']}

**🔥 なぜ今このテーマが熱いのか？**
{theme['trend']}

**💡 この記事で読者に提供できる価値**
{theme['value']}

---
"""
    
    return markdown

def main():
    """メイン実行関数"""
    print("🔍 技術トレンドを調査中...")
    themes = generate_theme_proposals()
    
    print("📝 記事テーマ案を生成中...")
    markdown_content = format_proposals(themes)
    
    # ファイルに保存
    with open("theme_proposals.md", "w", encoding="utf-8") as f:
        f.write(markdown_content)
    
    print("✅ テーマ提案を生成しました！")
    print("📄 詳細は 'theme_proposals.md' を確認してください")
    
    # コンソールにも表示
    print("\n" + "="*50)
    print(markdown_content)
    print("="*50)

if __name__ == "__main__":
    main()
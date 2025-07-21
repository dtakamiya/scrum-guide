#!/usr/bin/env python3
"""
ステップ4: note用ハッシュタグの提案
記事の内容とターゲット読者層を踏まえてハッシュタグを提案
"""

from datetime import datetime

def generate_hashtags():
    """記事に適したハッシュタグを生成"""
    
    # 基本ハッシュタグ（技術系）
    basic_tech_tags = [
        "#DDD",
        "#オニオンアーキテクチャ", 
        "#CleanArchitecture",
        "#アーキテクチャ設計",
        "#設計パターン"
    ]
    
    # 対象読者向けハッシュタグ
    target_audience_tags = [
        "#初級エンジニア",
        "#エンジニア初心者",
        "#プログラミング学習"
    ]
    
    # 実践・学習系ハッシュタグ
    practical_tags = [
        "#実践",
        "#TypeScript",
        "#依存性注入",
        "#テスタビリティ"
    ]
    
    # キャリア・成長系ハッシュタグ
    career_tags = [
        "#エンジニアキャリア",
        "#技術力向上",
        "#コード設計"
    ]
    
    # コミュニティ・拡散系ハッシュタグ
    community_tags = [
        "#プログラミング",
        "#ソフトウェア開発",
        "#技術記事"
    ]
    
    # 全てのハッシュタグを結合
    all_hashtags = basic_tech_tags + target_audience_tags + practical_tags + career_tags + community_tags
    
    return all_hashtags

def format_hashtags(hashtags):
    """ハッシュタグをマークダウン形式でフォーマット"""
    
    markdown = f"""# 🏷️ note用ハッシュタグ提案

**生成日時:** {datetime.now().strftime('%Y年%m月%d日 %H:%M')}

---

## 📝 推奨ハッシュタグ（10個）

### 技術系ハッシュタグ
{hashtags[0]}
{hashtags[1]}
{hashtags[2]}
{hashtags[3]}
{hashtags[4]}

### 対象読者向けハッシュタグ
{hashtags[5]}
{hashtags[6]}
{hashtags[7]}

### 実践・学習系ハッシュタグ
{hashtags[8]}
{hashtags[9]}
{hashtags[10]}
{hashtags[11]}

### キャリア・成長系ハッシュタグ
{hashtags[12]}
{hashtags[13]}
{hashtags[14]}

### コミュニティ・拡散系ハッシュタグ
{hashtags[15]}
{hashtags[16]}
{hashtags[17]}

---

## 📊 ハッシュタグ分析

### 技術系（5個）
- DDD、オニオンアーキテクチャ、Clean Architectureなど、記事の核心技術を表現
- アーキテクチャ設計に興味のあるエンジニアにアピール

### 対象読者向け（3個）
- 初級エンジニア、初心者向けの内容であることを明確化
- 学習中のエンジニアが検索しやすいキーワード

### 実践・学習系（4個）
- 実践的な内容、TypeScript、依存性注入など具体的な技術要素
- 実際に使えるスキルを学べることをアピール

### キャリア・成長系（3個）
- エンジニアの成長、キャリアアップに関心のある読者にアピール
- 技術力向上を目指すエンジニアが検索しやすい

### コミュニティ・拡散系（3個）
- プログラミング、ソフトウェア開発の広いコミュニティにアピール
- 技術記事としての拡散を促進

---

## 🎯 使用のコツ

1. **バランスの取れた組み合わせ**: 技術系、対象読者向け、実践系をバランスよく使用
2. **トレンドを意識**: 現在注目されている技術キーワードを含める
3. **検索性を重視**: 読者が検索しそうなキーワードを選定
4. **拡散性を考慮**: シェアされやすいハッシュタグを組み合わせ

---

## 📝 コピー用テキスト

```
{hashtags[0]} {hashtags[1]} {hashtags[2]} {hashtags[3]} {hashtags[4]} {hashtags[5]} {hashtags[6]} {hashtags[7]} {hashtags[8]} {hashtags[9]} {hashtags[10]} {hashtags[11]} {hashtags[12]} {hashtags[13]} {hashtags[14]} {hashtags[15]} {hashtags[16]} {hashtags[17]}
```

"""
    
    return markdown

def main():
    """メイン実行関数"""
    print("🏷️ ハッシュタグ提案を開始します")
    
    # ハッシュタグを生成
    print("📝 ハッシュタグを生成中...")
    hashtags = generate_hashtags()
    
    # フォーマットして保存
    markdown_content = format_hashtags(hashtags)
    
    with open("hashtag_proposals.md", "w", encoding="utf-8") as f:
        f.write(markdown_content)
    
    print("✅ ハッシュタグ提案を生成しました！")
    print("📄 詳細は 'hashtag_proposals.md' を確認してください")
    
    # コンソールにも表示
    print("\n" + "="*50)
    print("🏷️ 推奨ハッシュタグ（18個）")
    print("="*50)
    for i, hashtag in enumerate(hashtags, 1):
        print(f"{i:2d}. {hashtag}")
    print("="*50)

if __name__ == "__main__":
    main()
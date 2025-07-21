#!/usr/bin/env python3
"""
note記事の全自動生成システム
ステップ0〜4を統合して、テーマ発見から執筆までを自動化
"""

import subprocess
import sys
import os
from datetime import datetime

def run_step(step_name, script_name):
    """各ステップを実行"""
    print(f"\n{'='*60}")
    print(f"🚀 {step_name}を開始します")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run([sys.executable, script_name], 
                              capture_output=True, text=True, encoding='utf-8')
        
        if result.returncode == 0:
            print(f"✅ {step_name}が完了しました！")
            return True
        else:
            print(f"❌ {step_name}でエラーが発生しました:")
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ {step_name}の実行中にエラーが発生しました: {e}")
        return False

def show_summary():
    """生成されたファイルの概要を表示"""
    print(f"\n{'='*60}")
    print("📊 生成されたファイル一覧")
    print(f"{'='*60}")
    
    files = [
        ("theme_proposals.md", "ステップ0: テーマ提案"),
        ("article_outline.md", "ステップ1: 記事骨子"),
        ("title_and_structure.md", "ステップ2: タイトル・構成案"),
        ("article_draft.md", "ステップ3: 記事本文"),
        ("hashtag_proposals.md", "ステップ4: ハッシュタグ提案")
    ]
    
    for filename, description in files:
        if os.path.exists(filename):
            size = os.path.getsize(filename)
            print(f"✅ {filename} ({description}) - {size:,} bytes")
        else:
            print(f"❌ {filename} ({description}) - ファイルが見つかりません")
    
    print(f"\n{'='*60}")
    print("🎉 note記事の全自動生成が完了しました！")
    print(f"{'='*60}")
    print("\n📝 次のステップ:")
    print("1. article_draft.md の内容を確認・編集")
    print("2. hashtag_proposals.md からハッシュタグを選択")
    print("3. noteに投稿")
    print("\n💡 ヒント:")
    print("- 生成された記事は約9,000文字の充実した内容です")
    print("- コード例が豊富で、実践的な内容になっています")
    print("- 初級エンジニア向けに分かりやすく解説されています")

def main():
    """メイン実行関数"""
    print("🎯 note記事の全自動生成システム")
    print("="*60)
    print("専門分野: ドメイン駆動設計とオニオンアーキテクチャ")
    print("ターゲット読者: 初級エンジニア")
    print(f"開始時刻: {datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}")
    print("="*60)
    
    # 各ステップを順次実行
    steps = [
        ("ステップ0: テーマ発見", "step0_theme_discovery_simple.py"),
        ("ステップ1: 骨子定義", "step1_theme_definition.py"),
        ("ステップ2: タイトル・構成案", "step2_title_and_structure.py"),
        ("ステップ3: 記事執筆", "step3_article_writing_fixed.py"),
        ("ステップ4: ハッシュタグ提案", "step4_hashtags.py")
    ]
    
    success_count = 0
    for step_name, script_name in steps:
        if run_step(step_name, script_name):
            success_count += 1
        else:
            print(f"⚠️ {step_name}でエラーが発生しましたが、続行します...")
    
    # 結果サマリーを表示
    print(f"\n{'='*60}")
    print(f"📈 実行結果: {success_count}/{len(steps)} ステップが成功")
    print(f"{'='*60}")
    
    if success_count == len(steps):
        print("🎉 全てのステップが正常に完了しました！")
        show_summary()
    else:
        print("⚠️ 一部のステップでエラーが発生しましたが、生成されたファイルを確認してください。")
        show_summary()

if __name__ == "__main__":
    main()
# リサーチレポート：スクラムのトラブルシューティング Part 3

## 情報源3: スクラムを失敗させる方法 (Ryuzee.com)

URL: https://www.ryuzee.com/contents/blog/3236

### 1. 主要な論点（失敗させる10の方法）

本記事は、海外のブログ記事 "How to make Scrum fail" を翻訳・紹介する形で、スクラムが失敗に至る具体的な10のアンチパターンを簡潔にリストアップしている。

#### 1. ふりかえり（レトロスペクティブ）をしない／形骸化している

*   **問題**: チームが改善するための最も重要な機会である「ふりかえり」を実施しないか、実施しても形式的で、うまくいったこと・改善できることについての率直な議論が行われない。
*   **示唆**: 失敗から学ばないチームは成長しない。

#### 2. ダメなプロダクトオーナー

*   **問題**: プロダクトオーナー（PO）が以下のような状態にある。
    *   プロジェクトに十分な時間を割けない。
    *   スプリントプランニングやふりかえりに参加しない。
    *   開発チームの責任であるタスクの見積もりに口を出す。
    *   ビジネスの優先順位ではなく、個人的な好みなどでバックログを並び替える。
    *   明確なビジョンや計画を持っていない。
    *   PBIを開発チームが理解できるレベルまで具体化できない。
    *   スプリントの途中でバックログの変更を要求する。
*   **示唆**: POはビジネス価値の最大化に責任を持つ重要な役割であり、その不在や機能不全はプロジェクトの方向性を見失わせる。

#### 3. ダメなスクラムマスター

*   **問題**: スクラムマスター（SM）が以下のような状態にある。
    *   チームを自己組織化させるのではなく、「管理者」として振る舞い、指示を出す。
    *   チーム内の意見対立に対して、最終決定を下すといった介入をしすぎる。
    *   チームが直面する障害を優先順位付けして、積極的に排除しようとしない。
    *   個々のメンバーにタスクを割り当てる（チームが自律的に選択するのを妨げる）。
*   **示唆**: SMはサーバントリーダーであり、チームの自律性を尊重し、障害を取り除くことに専念すべきである。

#### 4. スクラムイベントが長すぎる

*   **問題**: デイリースクラム、スプリントプランニング、ふりかえりといったイベントが、本来の目的から外れて長時間の議論の場となり、タイムボックスを守れていない。
*   **示唆**: イベントの本質（デイリースクラムなら3つの質問の共有）に集中し、時間を厳守することで、リズムと集中を保つ。

#### 5. 「完成の定義」が間違っている

*   **問題**: スプリントの成果物が、スプリントレビューの時点で「リリース可能」な状態になっていない。テストが自動化されていなかったり、品質基準が満たされていない。
*   **示唆**: 「完成」とは、いつでも出荷できるレベルの品質を担保している状態を指す。これがなければ、スプリントの意味が薄れる。

#### 6. ベロシティを計測していない

*   **問題**: チームの生産性（ベロシティ）を計測しておらず、その変化に対するアクションが取られていない。
*   **示唆**: ベロシティの停滞は問題のサインであり、SMは根本原因（例：「なぜなぜ分析」）を特定し、改善を促すべきである。

#### 7. スプリント内ウォーターフォール

*   **問題**: スプリントの終わりに、多数のアイテムが「75%完了」のような中途半端な状態で残っている。これは、スプリント内で「分析→設計→実装→テスト」というミニウォーターフォールを行っている兆候。
*   **示唆**: 少数のアイテムでも良いので、一つひとつを「100%完了」させることに集中すべきである。

#### 8. 技術的負債の放置

*   **問題**: リファクタリングやバグ修正を後回しにし、技術的負債を積み上げている。
*   **示唆**: 技術的負債は将来の開発速度を確実に低下させる。負債は発生後、できるだけ早く返済しなければならない。

#### 9. 割り込みが多すぎる

*   **問題**: POを経由せず、ステークホルダーなどが直接開発チームに機能追加や修正を依頼する。
*   **示唆**: チームの集中を守ることが重要。全ての要求はPOを通じてプロダクトバックログで一元管理し、優先順位付けされるべきである。

#### 10. 分析やドキュメントが皆無

*   **問題**: 「アジャイルではドキュメントは不要」と極端に解釈し、必要な分析やドキュメント作成を一切行わない。
*   **示唆**: スクラムは「Just Enough（必要十分）」な分析とドキュメントを推奨している。特にPBIは、チームが見積もりとタスク分割ができるレベルまで、継続的に詳細化される必要がある。

### 2. まとめ

この記事は、スクラムの各ロール（PO, SM, 開発チーム）と各イベント、そして重要な概念（完成の定義, 技術的負債など）において、**何を「しない」べきか**を逆説的に示すことで、スクラムを成功させるための要点を浮き彫りにしている。

それぞれの項目は、スクラムの原則から逸脱した具体的な行動を示しており、チームが自分たちの現状を振り返るための優れた**「チェックリスト」**として活用できる。簡潔でありながら、スクラム運営における本質的な失敗の原因を的確に網羅している。

[情報源3] 
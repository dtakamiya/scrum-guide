## 9. アンチパターンと対策

| アンチパターン | なぜ問題か？ | 対策 |
| :--- | :--- | :--- |
| **アウトプット指標（ベロシティ等）のみを追う** | 価値のない機能を大量生産する「More-on-more-on」に陥る。忙しいだけで成果が出ない。 | アウトカム指標（顧客満足度など）を主とし、アウトプットは参考情報として扱う。 |
| **KPIを個人の評価・人事考課と直結させる** | メンバーは自己防衛に走り、正直なデータを報告しなくなる。チーム内の協力関係も崩壊する。 | KPIはあくまで「チームの改善」のためのツールと明確に位置づける。個人の評価とは切り離す。 |
| **マネージャーがトップダウンでKPIを決定する** | チームはKPIにオーナーシップを持てず、「やらされ仕事」になる。現場の実態と乖離した指標になりがち。 | KPIの設計プロセスにチームを巻き込み、自分たちの指標として選んでもらう。 |
| **一度決めたKPIを絶対視し、見直さない** | ビジネス環境やプロダクトのフェーズが変わると、KPIも陳腐化する。 | 定期的なレトロスペクティブなどで、KPIが今も有効か、チームで常に見直し、改善・廃止する。 |
| **指標の背景を理解せず、数字だけを比較する** | 「チームAはベロシティが20なのに、チームBは15で低い」といった不毛な比較は、チーム間の対立を煽るだけ。 | 各指標が持つ意味、ばらつきの背景を理解し、対話のきっかけとして使う。 |
| **マルチベンダー環境で各社が独自のKPIを持つ** | 各ベンダーが部分最適に走り、プロジェクト全体としての一体感が失われる。問題発生時に責任のなすりつけ合いが始まる。 | プロジェクト全体の成功を定義する「共有KPI」を設定し、全員でその達成にコミットする。 |

## 10. FAQ（よくある質問）

*   **Q: 心理的安全性をKPIとして設定すべきでしょうか？**
    *   A: これには両論あります。**賛成意見**としては「測定することで、組織として改善に取り組む本気度を示せる」というものがあります。一方、**反対意見**としては「スコアを良くすることが目的化し、管理職がメンバーに良い回答を強要するなど、本末転倒な事態になりかねない」という懸念があります。重要なのは、サーベイの結果を人事評価などに使わず、あくまで対話と改善のきっかけとして使うというコンセンサスを、組織全体で形成することです。

*   **Q: どのようなツールを使えば良いですか？**
    *   A: まずはJiraやAsanaなど、普段使っているタスク管理ツールの標準機能から始めるのが手軽です。データが溜まってきたら、TableauやLooker Studio (旧Google Data Studio)などで複数の情報源を統合し、チーム独自のダッシュボードを構築するのが良いでしょう。目的や成熟度に合わせてツールを選ぶことが重要です。

*   **Q: KPIが多すぎて運用できません。どうすれば？**
    *   A: 「計測の罠」に陥っています。今すぐ計測をやめても誰も困らない指標は、廃止すべきです。EBMの4つの価値領域（CV, UV, A2I, T2M）それぞれについて、最も重要な指標を1つか2つに絞り込むことから始めましょう。「Less is More（少ない方が豊かである）」は、KPI運用においても真実です。

## 11. テンプレート・チェックリスト

### ● 心理的安全性セルフチェックリスト

チームのレトロスペクティブなどで、定期的に以下の項目について対話してみましょう。（はい／いいえ／部分的に）

| チェック項目 | はい | いいえ | 部分的に |
| :--- | :-: | :-: | :---: |
| 1. チームの中でミスをすると、大抵の場合、非難される。 | | | |
| 2. チームのメンバーは、課題や難しい問題を提起することができる。 | | | |
| 3. チームのメンバーは、自分と違うということを理由に、他者を拒絶することがある。| | | |
| 4. チームに対してリスクのある行動をとっても安全である。 | | | |
| 5. チームの他のメンバーに助けを求めることは難しい。 | | | |
| 6. チームの誰もが、他人の努力を意図的に損なうような行動をしない。 | | | |
| 7. チームメンバーと仕事をするとき、自分のスキルと才能が尊重され、活かされていると感じる。| | | |
*(Amy Edmondson氏の論文で用いられる7つの質問より抜粋・改変)*

## 12. 参考リンク

本ガイドの作成にあたり、以下の主要な情報源を参考にしました。より深く学びたい方は、原典を参照することをお勧めします。

*   **EBM (Evidence-Based Management):**
    *   [Scrum.org EBM Guide (公式ガイド)](https://www.scrum.org/resources/evidence-based-management-guide)
    *   [Workpath: EBM and OKRs](https://www.workpath.com/magazine/ebm-okrs)
*   **Flow Metrics:**
    *   [Scrum.org: Flow Metrics for Scrum Teams](https://www.scrum.org/resources/flow-metrics-scrum-teams-whitepaper)
    *   [Agile Seekers: Advanced Flow Metrics](https://agileseekers.com/en/flow-metrics-for-advanced-scrum-masters-and-agile-coaches/)
*   **Outcome vs Output:**
    *   [ProdPad: The Difference Between Output and Outcome](https://www.prodpad.com/blog/product-management-output-vs-outcome/)
    *   [Aditi Agarwal: Agile Metrics - Output Vs Outcome](https://authoraditiagarwal.com/agile-metrics-output-vs-outcome-measure-what-matters/)
*   **Multi-Vendor Projects:**
    *   [Flevy: Cross-Functional Collaboration KPIs](https://flevy.com/blog/the-power-of-kpis-in-driving-cross-functional-collaboration/)
*   **Continuous Improvement Culture:**
    *   [Agile Sherpas: 8 Ways to Create a Culture of Continuous Improvement](https://www.agilesherpas.com/blog/8-ways-to-create-a-culture-of-continuous-improvement)
*   **Agile KPI Dashboards:**
    *   [Atlassian: Five agile KPI metrics you won't hate](https://www.atlassian.com/agile/project-management/metrics)
    *   [SlideTeam: Top 15 Agile KPI Metrics Dashboard Templates](https://www.slideteam.net/blog/top-15-agile-kpi-metrics-dashboard-templates-to-ensure-project-success)
*   **Psychological Safety & KPIs:**
    *   [Stacey Barr: Psychological Safety for Successful KPI Transformations](https://www.linkedin.com/pulse/psychological-safety-successful-kpi-transformations-stacey-barr)
    *   [IMERGEY: Psychological Safety as a KPI](https://www.imergey.com/blog/psychological-safety-as-a-kpi-its-impact-on-team-productivity-and-innovation/) 
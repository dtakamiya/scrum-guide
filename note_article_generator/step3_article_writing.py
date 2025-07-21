#!/usr/bin/env python3
"""
ステップ3: 記事本文の執筆
構成案に基づいて魅力的な記事本文を生成
"""

from datetime import datetime

def generate_article_content():
    """記事本文を生成"""
    
    article = f"""# 【完全版】初級エンジニアが30分で理解するオニオンアーキテクチャ実践ガイド

*執筆日: {datetime.now().strftime('%Y年%m月%d日')}*

---

## はじめに

こんにちは！初級エンジニアの皆さん、アーキテクチャ設計に苦手意識はありませんか？

「オニオンアーキテクチャって聞いたことはあるけど、実際にどう使えばいいの？」
「DDDとオニオンアーキテクチャの関係がよくわからない」
「実務でどうやって適用すればいいの？」

そんな悩みを抱えている方も多いのではないでしょうか。

この記事では、**初級エンジニアの視点**から、オニオンアーキテクチャの基本概念から実践的な実装まで、**30分で理解できる**ように解説していきます。

実際のコード例も豊富に用意しているので、読了後には自分のプロジェクトで即座に適用できるようになるはずです！

---

## 1. なぜ今オニオンアーキテクチャが重要なのか？

### 従来の設計手法の課題

まず、なぜオニオンアーキテクチャが必要なのかを理解しましょう。

従来の**データ駆動設計**では、以下のような問題が発生しがちでした：

```javascript
// 従来の設計例（問題のあるコード）
class UserService {{
    async createUser(userData) {{
        // データベースに直接アクセス
        const user = await db.users.create(userData);
        
        // ビジネスロジックが散らばっている
        if (userData.email.includes('@company.com')) {{
            await sendWelcomeEmail(user.email);
        }}
        
        return user;
    }}
}}
```

この設計には以下の問題があります：

- **密結合**: ビジネスロジックとデータアクセスが混在
- **テスタビリティの低下**: データベースに依存するため単体テストが困難
- **保守性の悪化**: 変更時の影響範囲が広い

### オニオンアーキテクチャが解決する問題

オニオンアーキテクチャは、これらの問題を以下のように解決します：

1. **関心の分離**: ビジネスロジックとインフラストラクチャを明確に分離
2. **依存関係の管理**: 内側のレイヤーが外側のレイヤーに依存しない
3. **テスタビリティの向上**: モックやスタブを使った単体テストが容易
4. **保守性の向上**: 変更の影響範囲を最小限に抑制

---

## 2. オニオンアーキテクチャの基本概念

### レイヤー構造の理解

オニオンアーキテクチャは、**玉ねぎの層**のように同心円状のレイヤー構造になっています：

```
┌─────────────────────────────────────┐
│           Presentation Layer        │ ← ユーザーインターフェース
├─────────────────────────────────────┤
│           Application Layer         │ ← ユースケース
├─────────────────────────────────────┤
│           Domain Layer             │ ← ビジネスロジック（中心）
├─────────────────────────────────────┤
│         Infrastructure Layer       │ ← データベース、外部API
└─────────────────────────────────────┘
```

### 依存関係の方向性

重要なのは、**依存関係の方向性**です：

- **内側のレイヤー**（Domain）は**外側のレイヤー**に依存しない
- **外側のレイヤー**は**内側のレイヤー**に依存する
- 依存関係は**内側に向かう**

これにより、ビジネスロジックが技術的な詳細から独立し、**変更に強い**アーキテクチャが実現できます。

---

## 3. 実際のコードで理解するオニオンアーキテクチャ

### サンプルプロジェクト：ユーザー管理システム

実際のコード例で理解を深めましょう。シンプルなユーザー管理システムを例に、各レイヤーの役割を見ていきます。

#### Domain Layer（ドメイン層）

```typescript
// domain/entities/User.ts
export class User {{
    constructor(
        private readonly id: string,
        private readonly email: string,
        private readonly name: string,
        private readonly createdAt: Date
    ) {{}}

    // ビジネスルール
    isCompanyEmail(): boolean {{
        return this.email.includes('@company.com');
    }}

    canSendWelcomeEmail(): boolean {{
        return this.isCompanyEmail() && this.createdAt > new Date('2024-01-01');
    }}
}}

// domain/repositories/UserRepository.ts
export interface UserRepository {{
    save(user: User): Promise<void>;
    findById(id: string): Promise<User | null>;
    findByEmail(email: string): Promise<User | null>;
}}
```

#### Application Layer（アプリケーション層）

```typescript
// application/useCases/CreateUserUseCase.ts
export class CreateUserUseCase {{
    constructor(
        private userRepository: UserRepository,
        private emailService: EmailService
    ) {{}}

    async execute(command: CreateUserCommand): Promise<User> {{
        // ビジネスロジックの実行
        const user = new User(
            generateId(),
            command.email,
            command.name,
            new Date()
        );

        // ドメインルールの確認
        if (user.canSendWelcomeEmail()) {{
            await this.emailService.sendWelcomeEmail(user.email);
        }}

        await this.userRepository.save(user);
        return user;
    }}
}}
```

#### Infrastructure Layer（インフラストラクチャ層）

```typescript
// infrastructure/repositories/UserRepositoryImpl.ts
export class UserRepositoryImpl implements UserRepository {{
    constructor(private db: Database) {{}}

    async save(user: User): Promise<void> {{
        await this.db.users.create({{
            id: user.id,
            email: user.email,
            name: user.name,
            createdAt: user.createdAt
        }});
    }}

    async findById(id: string): Promise<User | null> {{
        const userData = await this.db.users.findById(id);
        if (!userData) return null;
        
        return new User(
            userData.id,
            userData.email,
            userData.name,
            userData.createdAt
        );
    }}
}}
```

---

## 4. 依存性注入（DI）の実践

### DIコンテナの活用

依存性注入を活用することで、さらに柔軟でテスタブルなコードが書けます：

```typescript
// infrastructure/di/container.ts
import { Container } from 'inversify';

const container = new Container();

// インターフェースと実装の紐付け
container.bind<UserRepository>('UserRepository').to(UserRepositoryImpl);
container.bind<EmailService>('EmailService').to(EmailServiceImpl);

export {{ container }};

// application/useCases/CreateUserUseCase.ts
@injectable()
export class CreateUserUseCase {{
    constructor(
        @inject('UserRepository') private userRepository: UserRepository,
        @inject('EmailService') private emailService: EmailService
    ) {{}}
    
    // ... 実装
}}
```

### テスタビリティの向上

DIにより、単体テストが容易になります：

```typescript
// tests/CreateUserUseCase.test.ts
describe('CreateUserUseCase', () => {{
    it('should create user and send welcome email for company email', async () => {{
        // モックの準備
        const mockUserRepository = {{
            save: jest.fn(),
            findById: jest.fn(),
            findByEmail: jest.fn()
        }};
        
        const mockEmailService = {{
            sendWelcomeEmail: jest.fn()
        }};

        const useCase = new CreateUserUseCase(mockUserRepository, mockEmailService);
        
        // テスト実行
        const result = await useCase.execute({{
            email: 'test@company.com',
            name: 'Test User'
        }});

        // 検証
        expect(mockUserRepository.save).toHaveBeenCalled();
        expect(mockEmailService.sendWelcomeEmail).toHaveBeenCalled();
    }});
}});
```

---

## 5. 実践的な設計パターン

### リポジトリパターン

データアクセスの抽象化にリポジトリパターンを使用します：

```typescript
// domain/repositories/UserRepository.ts
export interface UserRepository {{
    save(user: User): Promise<void>;
    findById(id: string): Promise<User | null>;
    findByEmail(email: string): Promise<User | null>;
    findAll(): Promise<User[]>;
    delete(id: string): Promise<void>;
}}
```

### ファクトリーパターン

複雑なオブジェクトの生成にファクトリーパターンを使用：

```typescript
// domain/factories/UserFactory.ts
export class UserFactory {{
    static create(command: CreateUserCommand): User {{
        return new User(
            generateId(),
            command.email,
            command.name,
            new Date()
        );
    }}

    static createFromData(data: UserData): User {{
        return new User(
            data.id,
            data.email,
            data.name,
            data.createdAt
        );
    }}
}}
```

### ドメインサービス

複数のエンティティにまたがるビジネスロジックにはドメインサービスを使用：

```typescript
// domain/services/UserDomainService.ts
export class UserDomainService {{
    constructor(private userRepository: UserRepository) {{}}

    async isEmailUnique(email: string): Promise<boolean> {{
        const existingUser = await this.userRepository.findByEmail(email);
        return existingUser === null;
    }}

    async validateUserCreation(command: CreateUserCommand): Promise<void> {{
        if (!await this.isEmailUnique(command.email)) {{
            throw new Error('Email already exists');
        }}
    }}
}}
```

---

## 6. よくある失敗と回避方法

### 失敗パターン1: ドメインロジックの漏洩

**問題**: ビジネスロジックがアプリケーション層やインフラ層に散らばる

```typescript
// ❌ 悪い例
class UserService {{
    async createUser(data) {{
        // ドメインロジックがアプリケーション層にある
        if (data.email.includes('@company.com')) {{
            // ビジネスルールがここにある
        }}
    }}
}}
```

**解決策**: ドメインロジックは必ずドメイン層に配置する

```typescript
// ✅ 良い例
class User {{
    isCompanyEmail(): boolean {{
        return this.email.includes('@company.com');
    }}
}}
```

### 失敗パターン2: 依存関係の逆転

**問題**: 内側のレイヤーが外側のレイヤーに依存してしまう

```typescript
// ❌ 悪い例
class User {{
    constructor() {{
        // ドメイン層がインフラ層に依存している
        this.db = new Database();
    }}
}}
```

**解決策**: 依存関係は必ず内側に向ける

```typescript
// ✅ 良い例
interface UserRepository {{
    save(user: User): Promise<void>;
}}

class User {{
    // ドメイン層はインターフェースにのみ依存
}}
```

### 失敗パターン3: 過度な抽象化

**問題**: 必要以上に複雑な抽象化を行い、理解しにくくなる

**解決策**: YAGNI原則（You Aren't Gonna Need It）に従い、必要最小限の抽象化にとどめる

---

## 7. まとめ：次のステップ

### 学習の振り返り

この記事で学んだこと：

1. **オニオンアーキテクチャの基本概念**: レイヤー構造と依存関係の方向性
2. **実践的な実装方法**: 実際のコード例での理解
3. **依存性注入の活用**: テスタビリティの向上
4. **設計パターンの適用**: リポジトリ、ファクトリー、ドメインサービス
5. **よくある失敗の回避**: 実務での注意点

### 実際のプロジェクトでの適用方法

1. **段階的な導入**: 既存のコードを一度に書き換えるのではなく、新機能から適用
2. **チームでの学習**: チーム全体でアーキテクチャの理解を深める
3. **継続的な改善**: 実装しながら学び、徐々に改善していく

### 次の学習ステップ

- **DDDの詳細**: エンティティ、値オブジェクト、集約の概念
- **CQRS**: コマンド・クエリ責任分離パターン
- **イベントソーシング**: イベント駆動アーキテクチャ
- **マイクロサービス**: 分散システムでのアーキテクチャ設計

---

## おわりに

オニオンアーキテクチャは、初級エンジニアにとって最初は複雑に感じるかもしれません。しかし、基本概念を理解し、実践的なコード例で学ぶことで、確実に身につけることができます。

重要なのは、**完璧を求めすぎない**ことです。最初は小さなプロジェクトから始めて、徐々に複雑なシステムに適用していきましょう。

この記事が、あなたのアーキテクチャ設計スキル向上の一助となれば幸いです！

**質問やフィードバックがあれば、コメントでお気軽にお聞かせください。**

---

*この記事は、初級エンジニア向けにオニオンアーキテクチャの基本から実践までを解説しました。次回は、より高度なDDDパターンについて詳しく解説する予定です。お楽しみに！*
"""
    
    return article

def save_article(article_content):
    """記事をファイルに保存"""
    
    with open("article_draft.md", "w", encoding="utf-8") as f:
        f.write(article_content)
    
    print("✅ 記事本文を生成しました！")
    print("📄 詳細は 'article_draft.md' を確認してください")

def main():
    """メイン実行関数"""
    print("📝 記事本文の執筆を開始します")
    
    # 記事本文を生成
    print("✍️ 記事本文を生成中...")
    article_content = generate_article_content()
    
    # ファイルに保存
    save_article(article_content)
    
    # 記事の概要を表示
    print("\n" + "="*50)
    print("📊 記事概要")
    print("="*50)
    print("タイトル: 【完全版】初級エンジニアが30分で理解するオニオンアーキテクチャ実践ガイド")
    print("文字数: 約{}文字".format(len(article_content)))
    print("セクション数: 7セクション")
    print("コード例: 豊富に含まれています")
    print("対象読者: 初級エンジニア")
    print("="*50)

if __name__ == "__main__":
    main()
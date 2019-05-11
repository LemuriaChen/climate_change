### 需求

#### 文献引用库 表与字段设计

* literature (数据库名)

```
CREATE DATABASE literature CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

* article (文章信息表)

```
CREATE TABLE article (
	article_id BIGINT NOT NULL PRIMARY KEY COMMENT '文章id，文章唯一标识符，主键',
	layer INT ( 11 ) COMMENT '抓取层级，种子文献列表为第0层',
	article_name VARCHAR ( 255 ) COMMENT '文章标题',
	article_type VARCHAR ( 255 ) COMMENT '文章类型，可为期刊、会议或其他类型',
	keywords VARCHAR ( 255 ) COMMENT '文章关键词',
	KeyWords_plus VARCHAR ( 255 ) COMMENT '文章领域分类',
	abstract text COMMENT '文章摘要',
	publish_date VARCHAR ( 255 ) COMMENT '文章发表日期',
	research_area VARCHAR ( 255 ) COMMENT '研究领域',
	journal_id BIGINT COMMENT '文章所在期刊的id',
	wos VARCHAR ( 255 ) COMMENT 'Web of Science检索号',
	wos_categories VARCHAR ( 255 ) COMMENT 'SCI检索号分类',
	doi VARCHAR ( 255 ) COMMENT '数字对象唯一标识符',
	ids_number VARCHAR ( 255 ) COMMENT 'SCI检索号，与wos类似',
	cited INT ( 11 ) COMMENT '在Web of Science核心合集被引用次数',
	created_time datetime NOT NULL COMMENT '记录创建时间',
FULLTEXT ( article_name, abstract )
) ENGINE = INNODB DEFAULT CHARSET = utf8mb4;
```

* author (作者信息表)

```
CREATE TABLE author (
	author_id BIGINT NOT NULL PRIMARY KEY COMMENT '作者id，作者唯一标识符，主键',
	author_name VARCHAR ( 255 ) COMMENT '作者名',
	article_id BIGINT NOT NULL COMMENT '文章id，文章唯一标识符',
	address VARCHAR ( 255 ) COMMENT '作者所在机构、国家等信息',
	researcher_id BIGINT COMMENT '研究者id',
	orc_id VARCHAR ( 255 ) COMMENT '学术出版物及学术产出的作者(即科研工作者)标识符',
	email VARCHAR ( 255 ) COMMENT '作者邮箱' 
) ENGINE = INNODB DEFAULT CHARSET = utf8mb4;
```

* co_author (作者合作信息表)

```
CREATE TABLE co_author ( 
	cooperation_id BIGINT NOT NULL PRIMARY KEY COMMENT '合作关系id，主键', 
	author_id BIGINT COMMENT '作者id，作者唯一标识符', 
	co_author_id BIGINT COMMENT '作者id，作者唯一标识符' 
) ENGINE = INNODB DEFAULT CHARSET = utf8mb4;
```

* journal (期刊/会议信息表)

```
CREATE TABLE journal ( 
	journal_id BIGINT NOT NULL PRIMARY KEY COMMENT '期刊id，期刊唯一标识符，主键', 
	journal_name VARCHAR ( 255 ) COMMENT '期刊名字', 
	research_domain VARCHAR ( 255 ) COMMENT '期刊涉及领域',
	publisher VARCHAR ( 255 ) COMMENT '出版社名称',
	country VARCHAR ( 255 ) COMMENT '期刊所在国家',
	issn VARCHAR ( 255 ) COMMENT '期刊ISSN号',
	eissn VARCHAR ( 255 ) COMMENT '期刊E-ISSN号'
) ENGINE = INNODB DEFAULT CHARSET = utf8mb4;
```

* journal_effect (期刊/会议影响因子表)

```
CREATE TABLE journal_effect ( 
	factor_id BIGINT NOT NULL PRIMARY KEY COMMENT 'factor id，主键',
	journal_id BIGINT COMMENT '期刊id，期刊唯一标识符', 
	impact_factor1 FLOAT COMMENT '2017年影响因子',
	impact_factor2 FLOAT COMMENT '近5年平均影响因子',
	research_domain VARCHAR ( 255 ) COMMENT '期刊涉及领域',
	journal_rank VARCHAR ( 255 ) COMMENT '期刊排名',
	quartile VARCHAR ( 255 ) COMMENT 'JCR分区'
) ENGINE = INNODB DEFAULT CHARSET = utf8mb4;
```

* funding (文章-基金对应表)

```
CREATE TABLE funding ( 
	funding_id BIGINT NOT NULL PRIMARY KEY COMMENT '基金号id，基金唯一标识符，主键', 
	funding_agency VARCHAR ( 255 ) COMMENT '基金资助机构',
	grant_number VARCHAR ( 255 ) COMMENT '基金号',
	article_id BIGINT COMMENT '文章id，文章唯一标识符'
) ENGINE = INNODB DEFAULT CHARSET = utf8mb4;
```

* citation （引用-被引用全表）

```
CREATE TABLE citation ( 
	cite_id BIGINT NOT NULL COMMENT '文章id，文章唯一标识符',
	cited_id BIGINT NOT NULL COMMENT '文章id，文章唯一标识符'
) ENGINE = INNODB DEFAULT CHARSET = utf8mb4;
```

* cite（引用表）

```
CREATE TABLE cite ( 
	cite_id BIGINT NOT NULL COMMENT '文章id，文章唯一标识符', 
	cited_id BIGINT NOT NULL COMMENT '文章id，文章唯一标识符'
) ENGINE = INNODB DEFAULT CHARSET = utf8mb4 PARTITION BY HASH ( cite_id ) PARTITIONS 20;
```

* cited (被引用表)

```
CREATE TABLE cited ( 
	cited_id BIGINT NOT NULL COMMENT '文章id，文章唯一标识符',
	cite_id BIGINT NOT NULL COMMENT '文章id，文章唯一标识符'
) ENGINE = INNODB DEFAULT CHARSET = utf8mb4 PARTITION BY HASH ( cited_id ) PARTITIONS 20;
```


#### 前端检索需求设计

* 文章标题模糊检索，''为所检索的字符串

```
SELECT * FROM article WHERE MATCH (article_name) AGAINST ('');
```

* 文章摘要模糊检索，''为所检索的字符串

```
SELECT * FROM article WHERE MATCH (abstract) AGAINST ('');
```

* 给定文章编号，查找该文章引用的所有文章

```
SELECT * FROM citation WHERE cite_id = ''
```

* 给定文章编号，查找引用该文章的所有文章

```
SELECT * FROM citation WHERE cited_id = ''
```

* 给定作者编号，查找该作者发表的所有文章

```
SELECT * FROM author WHERE author_id = ''
```




















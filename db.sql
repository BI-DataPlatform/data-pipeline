SET foreign_key_checks = 0;
DROP TABLE IF EXISTS `accounts`;
DROP TABLE IF EXISTS `family_accounts`;
DROP TABLE IF EXISTS `addresses`;
DROP TABLE IF EXISTS `favorites`;
DROP TABLE IF EXISTS `stores`;
DROP TABLE IF EXISTS `carts`;
DROP TABLE IF EXISTS `products`;
DROP TABLE IF EXISTS `orders`;
DROP TABLE IF EXISTS `alarms`;
DROP TABLE IF EXISTS `orderlines`;
DROP TABLE IF EXISTS `reviews`;
DROP TABLE IF EXISTS `review_tags`;
DROP TABLE IF EXISTS `replies`;
DROP TABLE IF EXISTS `deliveries`;
DROP TABLE IF EXISTS `dispatchers`;
DROP TABLE IF EXISTS `store_categories`;
DROP TABLE IF EXISTS `categories`;
DROP TABLE IF EXISTS `agencies`;
DROP TABLE IF EXISTS `delivery_informations`;
DROP TABLE IF EXISTS `order_status`;
SET foreign_key_checks = 1;

CREATE TABLE `accounts` (
	`id`	VARCHAR(64)	NOT NULL,
	`email`	VARCHAR(50)	NULL,
	`password`	VARCHAR(64)	NULL,
	`nickname`	VARCHAR(20)	NULL,
	`phone_number`	VARCHAR(16)	NULL,
	`virtual_number`	VARCHAR(16)	NULL,
	`payment`	VARCHAR(64)	NULL,
	`family_account_id`	VARCHAR(64)	NULL,
	`points`	INT	NULL,
	`rank`	VARCHAR(8)	NULL,
	`role`	VARCHAR(8)	NULL,
	`created_on`	TIMESTAMP	NULL,
	`last_updated_on`	TIMESTAMP	NULL
);

CREATE TABLE `family_accounts` (
	`id`	VARCHAR(64)	NOT NULL,
	`account_id`	VARCHAR(64)	NOT NULL,
	`payment`	VARCHAR(64)	NULL,
	`orders_left`	INT	NULL,
	`created_on`	TIMESTAMP	NULL,
	`last_updated_on`	TIMESTAMP	NULL
);

CREATE TABLE `addresses` (
	`id`	VARCHAR(64)	NOT NULL,
	`account_id`	VARCHAR(64)	NOT NULL,
	`is_current`	BOOLEAN	NULL,
	`name`	VARCHAR(20)	NULL,
	`first_address`	VARCHAR(100)	NULL,
	`second_address`	VARCHAR(100)	NULL,
	`favor`	VARCHAR(100)	NULL,
	`created_on`	TIMESTAMP	NULL,
	`last_updated_on`	TIMESTAMP	NULL
);

CREATE TABLE `favorites` (
	`id`	VARCHAR(64)	NOT NULL,
	`account_id`	VARCHAR(64)	NOT NULL,
	`store_id`	VARCHAR(64)	NOT NULL,
	`created_on`	TIMESTAMP	NULL,
	`last_updated_on`	TIMESTAMP	NULL
);

CREATE TABLE `stores` (
	`id`	VARCHAR(64)	NOT NULL,
	`status`	VARCHAR(10)	NULL,
	`name`	VARCHAR(100)	NULL,
	`address`	VARCHAR(200)	NULL,
	`business_hours`	VARCHAR(100)	NULL,
	`day_off`	VARCHAR(100)	NULL,
	`description`	TEXT	NULL,
	`min_orders`	INT	NULL,
	`max_distance`	INT	NULL,
	`phone_number`	VARCHAR(16)	NULL,
	`owner`	VARCHAR(20)	NULL,
	`taxpayer_address`	VARCHAR(200)	NULL,
	`taxpayer_id_number`	VARCHAR(12)	NULL,
	`ingredients`	TEXT	NULL,
	`created_on`	TIMESTAMP	NULL,
	`last_updated_on`	TIMESTAMP	NULL
);

CREATE TABLE `carts` (
	`id`	VARCHAR(64)	NOT NULL,
	`account_id`	VARCHAR(64)	NOT NULL,
	`product_id`	VARCHAR(64)	NOT NULL,
	`options`	TEXT	NULL,
	`amount`	INT	NULL,
	`created_on`	TIMESTAMP	NULL,
	`last_updated_on`	TIMESTAMP	NULL
);

CREATE TABLE `products` (
	`id`	VARCHAR(64)	NOT NULL,
	`store_id`	VARCHAR(64)	NOT NULL,
    `name`  VARCHAR(100) NULL,
	`options`	TEXT	NULL,
	`description`	VARCHAR(500)	NULL,
	`image`	VARCHAR(200)	NULL,
	`price`	INT	NULL,
	`created_on`	TIMESTAMP	NULL,
	`last_updated_on`	TIMESTAMP	NULL
);

CREATE TABLE `orders` (
	`id`	VARCHAR(64)	NOT NULL,
	`account_id`	VARCHAR(64)	NOT NULL,
	`store_id`	VARCHAR(64)	NOT NULL,
	`status`	VARCHAR(10)	NULL,
	`payment`	VARCHAR(64)	NULL,
	`delivery_type`	VARCHAR(12)	NULL,
	`delivery_id`	VARCHAR(64)	NULL,
	`address`	VARCHAR(200)	NULL,
	`phone_number`	VARCHAR(16)	NULL,
	`price`	INT	NULL,
	`delivery_fee`	INT	NULL,
	`total_price`	INT	NULL,
	`virtual_number`	VARCHAR(16)	NULL,
	`wants_disposables`	BOOLEAN	NULL,
	`favor_store`	VARCHAR(100)	NULL,
	`favor_delivery`	VARCHAR(100)	NULL,
	`created_on`	TIMESTAMP	NULL,
	`last_updated_on`	TIMESTAMP	NULL
);

CREATE TABLE `alarms` (
	`id`	VARCHAR(64)	NOT NULL,
	`account_id`	VARCHAR(64)	NOT NULL,
	`title`	VARCHAR(100)	NULL,
	`content`	VARCHAR(500)	NULL,
	`link`	VARCHAR(200)	NULL,
	`created_on`	TIMESTAMP	NULL,
	`last_updated_on`	TIMESTAMP	NULL
);

CREATE TABLE `orderlines` (
	`id`	VARCHAR(64)	NOT NULL,
	`order_id`	VARCHAR(64)	NOT NULL,
	`product_id`	VARCHAR(64)	NOT NULL,
	`options`	TEXT	NULL,
	`amount`	INT	NULL,
	`created_on`	TIMESTAMP	NULL,
	`last_updated_on`	TIMESTAMP	NULL
);

CREATE TABLE `reviews` (
	`id`	VARCHAR(64)	NOT NULL,
	`account_id`	VARCHAR(64)	NOT NULL,
	`store_id`	VARCHAR(64)	NOT NULL,
	`ratings_delivery`	TINYINT	NULL,
	`ratings_food`	TINYINT	NULL,
	`image`	VARCHAR(200)	NULL,
	`content`	VARCHAR(1000)	NULL,
	`reply_id`	VARCHAR(64)	NULL,
	`is_public`	BOOLEAN	NULL,
	`shows_orders`	BOOLEAN	NULL,
	`created_on`	TIMESTAMP	NULL,
	`last_updated_on`	TIMESTAMP	NULL
);

CREATE TABLE `review_tags` (
	`id`	VARCHAR(64)	NOT NULL,
	`review_id`	VARCHAR(64)	NOT NULL,
	`product_id`	VARCHAR(64)	NOT NULL,
	`recommend`	BOOLEAN	NULL,
	`comment`	VARCHAR(100)	NULL,
	`created_on`	TIMESTAMP	NULL,
	`last_updated_on`	TIMESTAMP	NULL
);

CREATE TABLE `replies` (
	`id`	VARCHAR(64)	NOT NULL,
	`content`	VARCHAR(1000)	NULL,
	`created_on`	TIMESTAMP	NULL,
	`last_updated_on`	TIMESTAMP	NULL
);

CREATE TABLE `deliveries` (
	`id`	VARCHAR(64)	NOT NULL,
	`status`	VARCHAR(10)	NULL,
	`delivery_type`	VARCHAR(12)	NULL,
	`dispatcher_id`	VARCHAR(64)	NOT NULL,
	`created_on`	TIMESTAMP	NULL,
	`last_updated_on`	TIMESTAMP	NULL
);

CREATE TABLE `dispatchers` (
	`id`	VARCHAR(64)	NOT NULL,
	`status`	VARCHAR(10)	NULL,
	`name`	VARCHAR(20)	NULL,
	`dispatcher_ride`	VARCHAR(20)	NULL,
	`phone_number`	VARCHAR(16)	NULL,
	`virtual_number`	VARCHAR(16)	NULL,
	`agency_id`	VARCHAR(64)	NOT NULL,
	`created_on`	TIMESTAMP	NULL,
	`last_updated_on`	TIMESTAMP	NULL
);

CREATE TABLE `store_categories` (
	`id`	VARCHAR(64)	NOT NULL,
	`store_id`	VARCHAR(64)	NOT NULL,
	`category_id`	VARCHAR(64)	NOT NULL,
	`created_on`	TIMESTAMP	NULL,
	`last_updated_on`	TIMESTAMP	NULL
);

CREATE TABLE `categories` (
	`id`	VARCHAR(64)	NOT NULL,
	`parent_category_id`	VARCHAR(64)	NULL,
	`name`	VARCHAR(20)	NULL,
	`description`	VARCHAR(100)	NULL,
	`created_on`	TIMESTAMP	NULL,
	`last_updated_on`	TIMESTAMP	NULL
);

CREATE TABLE `agencies` (
	`id`	VARCHAR(64)	NOT NULL,
	`name`	VARCHAR(100)	NULL,
	`created_on`	TIMESTAMP	NULL,
	`last_updated_on`	TIMESTAMP	NULL
);

CREATE TABLE `delivery_informations` (
	`id`	VARCHAR(64)	NOT NULL,
	`store_id`	VARCHAR(64)	NOT NULL,
	`delivery_type`	VARCHAR(12)	NULL,
	`min_fee`	INT	NULL,
	`max_fee`	INT	NULL,
	`created_on`	TIMESTAMP	NULL,
	`last_updated_on`	TIMESTAMP	NULL
);

CREATE TABLE `order_status` (
	`id`	VARCHAR(64)	NOT NULL,
	`order_id`	VARCHAR(64)	NOT NULL,
	`progress`	VARCHAR(10)	NULL,
	`dispatcher_location`	VARCHAR(200)	NULL,
	`dispatcer_latitude`	DOUBLE	NULL,
	`dispatcer_longtitude`	DOUBLE	NULL,
	`created_on`	TIMESTAMP	NULL,
	`last_updated_on`	TIMESTAMP	NULL
);

ALTER TABLE `accounts` ADD CONSTRAINT `PK_ACCOUNTS` PRIMARY KEY (
	`id`
);

ALTER TABLE `family_accounts` ADD CONSTRAINT `PK_FAMILY_ACCOUNTS` PRIMARY KEY (
	`id`
);

ALTER TABLE `addresses` ADD CONSTRAINT `PK_ADDRESSES` PRIMARY KEY (
	`id`
);

ALTER TABLE `favorites` ADD CONSTRAINT `PK_FAVORITES` PRIMARY KEY (
	`id`
);

ALTER TABLE `stores` ADD CONSTRAINT `PK_STORES` PRIMARY KEY (
	`id`
);

ALTER TABLE `carts` ADD CONSTRAINT `PK_CARTS` PRIMARY KEY (
	`id`
);

ALTER TABLE `products` ADD CONSTRAINT `PK_PRODUCTS` PRIMARY KEY (
	`id`
);

ALTER TABLE `orders` ADD CONSTRAINT `PK_ORDERS` PRIMARY KEY (
	`id`
);

ALTER TABLE `alarms` ADD CONSTRAINT `PK_ALARMS` PRIMARY KEY (
	`id`
);

ALTER TABLE `orderlines` ADD CONSTRAINT `PK_ORDERLINES` PRIMARY KEY (
	`id`
);

ALTER TABLE `reviews` ADD CONSTRAINT `PK_REVIEWS` PRIMARY KEY (
	`id`
);

ALTER TABLE `review_tags` ADD CONSTRAINT `PK_REVIEW_TAGS` PRIMARY KEY (
	`id`
);

ALTER TABLE `replies` ADD CONSTRAINT `PK_REPLIES` PRIMARY KEY (
	`id`
);

ALTER TABLE `deliveries` ADD CONSTRAINT `PK_DELIVERIES` PRIMARY KEY (
	`id`
);

ALTER TABLE `dispatchers` ADD CONSTRAINT `PK_DISPATCHERS` PRIMARY KEY (
	`id`
);

ALTER TABLE `store_categories` ADD CONSTRAINT `PK_STORE_CATEGORIES` PRIMARY KEY (
	`id`
);

ALTER TABLE `categories` ADD CONSTRAINT `PK_CATEGORIES` PRIMARY KEY (
	`id`
);

ALTER TABLE `agencies` ADD CONSTRAINT `PK_AGENCIES` PRIMARY KEY (
	`id`
);

ALTER TABLE `delivery_informations` ADD CONSTRAINT `PK_DELIVERY_INFORMATIONS` PRIMARY KEY (
	`id`
);

ALTER TABLE `order_status` ADD CONSTRAINT `PK_ORDER_STATUS` PRIMARY KEY (
	`id`
);

ALTER TABLE `accounts` ADD CONSTRAINT `FK_family_accounts_TO_accounts_1` FOREIGN KEY (
	`family_account_id`
)
REFERENCES `family_accounts` (
	`id`
);

ALTER TABLE `family_accounts` ADD CONSTRAINT `FK_accounts_TO_family_accounts_1` FOREIGN KEY (
	`account_id`
)
REFERENCES `accounts` (
	`id`
);

ALTER TABLE `addresses` ADD CONSTRAINT `FK_accounts_TO_addresses_1` FOREIGN KEY (
	`account_id`
)
REFERENCES `accounts` (
	`id`
);

ALTER TABLE `favorites` ADD CONSTRAINT `FK_accounts_TO_favorites_1` FOREIGN KEY (
	`account_id`
)
REFERENCES `accounts` (
	`id`
);

ALTER TABLE `favorites` ADD CONSTRAINT `FK_stores_TO_favorites_1` FOREIGN KEY (
	`store_id`
)
REFERENCES `stores` (
	`id`
);

ALTER TABLE `carts` ADD CONSTRAINT `FK_accounts_TO_carts_1` FOREIGN KEY (
	`account_id`
)
REFERENCES `accounts` (
	`id`
);

ALTER TABLE `carts` ADD CONSTRAINT `FK_products_TO_carts_1` FOREIGN KEY (
	`product_id`
)
REFERENCES `products` (
	`id`
);

ALTER TABLE `products` ADD CONSTRAINT `FK_stores_TO_products_1` FOREIGN KEY (
	`store_id`
)
REFERENCES `stores` (
	`id`
);

ALTER TABLE `orders` ADD CONSTRAINT `FK_accounts_TO_orders_1` FOREIGN KEY (
	`account_id`
)
REFERENCES `accounts` (
	`id`
);

ALTER TABLE `orders` ADD CONSTRAINT `FK_stores_TO_orders_1` FOREIGN KEY (
	`store_id`
)
REFERENCES `stores` (
	`id`
);

ALTER TABLE `orders` ADD CONSTRAINT `FK_deliveries_TO_orders_1` FOREIGN KEY (
	`delivery_id`
)
REFERENCES `deliveries` (
	`id`
);

ALTER TABLE `alarms` ADD CONSTRAINT `FK_accounts_TO_alarms_1` FOREIGN KEY (
	`account_id`
)
REFERENCES `accounts` (
	`id`
);

ALTER TABLE `orderlines` ADD CONSTRAINT `FK_orders_TO_orderlines_1` FOREIGN KEY (
	`order_id`
)
REFERENCES `orders` (
	`id`
);

ALTER TABLE `orderlines` ADD CONSTRAINT `FK_products_TO_orderlines_1` FOREIGN KEY (
	`product_id`
)
REFERENCES `products` (
	`id`
);

ALTER TABLE `reviews` ADD CONSTRAINT `FK_accounts_TO_reviews_1` FOREIGN KEY (
	`account_id`
)
REFERENCES `accounts` (
	`id`
);

ALTER TABLE `reviews` ADD CONSTRAINT `FK_stores_TO_reviews_1` FOREIGN KEY (
	`store_id`
)
REFERENCES `stores` (
	`id`
);

ALTER TABLE `reviews` ADD CONSTRAINT `FK_replies_TO_reviews_1` FOREIGN KEY (
	`reply_id`
)
REFERENCES `replies` (
	`id`
);

ALTER TABLE `review_tags` ADD CONSTRAINT `FK_reviews_TO_review_tags_1` FOREIGN KEY (
	`review_id`
)
REFERENCES `reviews` (
	`id`
);

ALTER TABLE `review_tags` ADD CONSTRAINT `FK_products_TO_review_tags_1` FOREIGN KEY (
	`product_id`
)
REFERENCES `products` (
	`id`
);

ALTER TABLE `deliveries` ADD CONSTRAINT `FK_dispatchers_TO_deliveries_1` FOREIGN KEY (
	`dispatcher_id`
)
REFERENCES `dispatchers` (
	`id`
);

ALTER TABLE `dispatchers` ADD CONSTRAINT `FK_agencies_TO_dispatchers_1` FOREIGN KEY (
	`agency_id`
)
REFERENCES `agencies` (
	`id`
);

ALTER TABLE `store_categories` ADD CONSTRAINT `FK_stores_TO_store_categories_1` FOREIGN KEY (
	`store_id`
)
REFERENCES `stores` (
	`id`
);

ALTER TABLE `store_categories` ADD CONSTRAINT `FK_categories_TO_store_categories_1` FOREIGN KEY (
	`category_id`
)
REFERENCES `categories` (
	`id`
);

ALTER TABLE `categories` ADD CONSTRAINT `FK_categories_TO_categories_1` FOREIGN KEY (
	`parent_category_id`
)
REFERENCES `categories` (
	`id`
);

ALTER TABLE `delivery_informations` ADD CONSTRAINT `FK_stores_TO_delivery_informations_1` FOREIGN KEY (
	`store_id`
)
REFERENCES `stores` (
	`id`
);

ALTER TABLE `order_status` ADD CONSTRAINT `FK_orders_TO_order_status_1` FOREIGN KEY (
	`order_id`
)
REFERENCES `orders` (
	`id`
);

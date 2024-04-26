CREATE TABLE IF NOT EXISTS accounts (
	id	VARCHAR(64)	NOT NULL primary key,
	email	VARCHAR(50)	NULL,
	password	VARCHAR(64)	NULL,
	nickname	VARCHAR(20)	NULL,
	phone_number	VARCHAR(16)	NULL,
	virtual_number	VARCHAR(16)	NULL,
	payment	VARCHAR(64)	NULL,
	family_account_id	VARCHAR(64)	NULL,
	points	INT	NULL,
	rank	VARCHAR(8)	NULL,
	role	VARCHAR(8)	NULL,
	created_on	TIMESTAMP	NULL,
	last_updated_on	TIMESTAMP	NULL
);

CREATE TABLE IF NOT EXISTS family_accounts (
	id	VARCHAR(64)	NOT NULL primary key,
	account_id	VARCHAR(64)	NOT NULL,
	payment	VARCHAR(64)	NULL,
	orders_left	INT	NULL,
	created_on	TIMESTAMP	NULL,
	last_updated_on	TIMESTAMP	NULL
);

CREATE TABLE IF NOT EXISTS addresses (
	id	VARCHAR(64)	NOT NULL primary key,
	account_id	VARCHAR(64)	NOT NULL,
	is_current	BOOLEAN	NULL,
	name	VARCHAR(20)	NULL,
	first_address	VARCHAR(100)	NULL,
	second_address	VARCHAR(100)	NULL,
	favor	VARCHAR(100)	NULL,
	created_on	TIMESTAMP	NULL,
	last_updated_on	TIMESTAMP	NULL
);

CREATE TABLE IF NOT EXISTS favorites (
	id	VARCHAR(64)	NOT NULL,
	account_id	VARCHAR(64)	NOT NULL,
	store_id	VARCHAR(64)	NOT NULL,
	created_on	TIMESTAMP	NULL,
	last_updated_on	TIMESTAMP	NULL
);
CREATE TABLE IF NOT EXISTS ORDERS (
	id	VARCHAR(64)	NOT NULL primary key,
	account_id	     VARCHAR(64)	NULL,
	store_id	     VARCHAR(64)	NULL,
	status           VARCHAR(10)	NULL,
	payment	         VARCHAR(64)	NULL,
	delivery_type	 VARCHAR(12)	NULL,
	delivery_id	     VARCHAR(64)	NULL,
	address	         VARCHAR(200)	NULL,
	phone_number	 VARCHAR(16)	NULL,
	price	         INT        	NULL,
	delivery_fee	 INT    	    NULL,
	total_price	     INT	        NULL,
	virtual_number	 VARCHAR(16)    NULL,
	wants_disposable BOOLEAN        NULL,
	favor_store      VARCHAR(100)   NULL,
	favor_delivery   VARCHAR(100)   NULL,
	created_on       TIMESTAMP      NULL,
	last_updated_on  TIMESTAMP      NULL
);

CREATE TABLE IF NOT EXISTS ORDER_STATUS (
	id	VARCHAR(64)	NOT NULL primary key,
	order_id    	    VARCHAR(64)	NOT NULL,
	progress    	    VARCHAR(10)	    NULL,
	dispatcher_location	VARCHAR(200)    NULL,
	dispatcher_latitude   DOUBLE        NULL,
	dispatcher_longtitude DOUBLE        NULL,
	created_on          TIMESTAMP       NULL,
	last_updated_on     TIMESTAMP       NULL
);

CREATE TABLE IF NOT EXISTS DELIVERIES (
	id	VARCHAR(64)	NOT NULL primary key,
	status           VARCHAR(10)	NULL,
	delivery_type	 VARCHAR(12)	NULL,
	dispatcher_id    VARCHAR(64)    NULL,
	created_on	     TIMESTAMP	    NULL,
	last_updated_on	 TIMESTAMP	    NULL
);
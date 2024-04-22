CREATE TABLE data.products (
    product_id VARCHAR(64),
    store_id VARCHAR(64),
    name VARCHAR(100),
    option_data TEXT,
    description VARCHAR(200),
    photo VARCHAR(200),
    price INTEGER,
    creation_date TIMESTAMP,
    update_date TIMESTAMP,
    PRIMARY KEY (product_id),
    FOREIGN KEY (store_id) REFERENCES store(store_id)
);

CREATE TABLE data.carts (
    cart_id VARCHAR(64),
    account_id VARCHAR(64),
    product_id VARCHAR(64),
    selected_option_quantity TEXT,
    quantity INTEGER,
    creation_date TIMESTAMP,
    update_date TIMESTAMP,
    PRIMARY KEY (cart_id),
    FOREIGN KEY (account_id) REFERENCES accounts(id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE data.orders (
    order_id VARCHAR(64),
    order_status VARCHAR(10),
    PRIMARY KEY (order_id)
);

CREATE TABLE data.order_line (
    order_line_id VARCHAR(64),
    order_id VARCHAR(64),
    product_id VARCHAR(64),
    selected_option_quantity TEXT,
    quantity INTEGER,
    creation_date TIMESTAMP,
    update_date TIMESTAMP,
    PRIMARY KEY (order_line_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
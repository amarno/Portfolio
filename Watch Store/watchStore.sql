
USE acm1123_theWatchStore;
-- SET FOREIGN_KEY_CHECKS=0;
-- DROP TABLE Cart;
-- DROP TABLE CartItem;

CREATE TABLE Item(
    sku INT(12), 
    name VARCHAR(200) NOT NULL,
    qty INT, -- in stock 
    price DECIMAL(6,2) NOT NULL,
    
    PRIMARY KEY (sku) 
);

CREATE TABLE Customer(
	id INT AUTO_INCREMENT, 
    fname VARCHAR(30) NOT NULL,
    lname VARCHAR(30) NOT NULL,
    email VARCHAR(80) NOT NULL,
    address VARCHAR(200) NOT NULL,
    zip INT NOT NULL,
    
    PRIMARY KEY (id)
);

CREATE TABLE Cart( 
	id INT AUTO_INCREMENT, 
    date DATETIME DEFAULT CURRENT_TIMESTAMP, 
    customer_id INT NOT NULL, 
    ordered BOOLEAN DEFAULT FALSE,
    shipped BOOLEAN DEFAULT FALSE, 
    
    PRIMARY KEY (id),
	FOREIGN KEY (customer_id) REFERENCES Customer (id) ON DELETE SET NULL

);

CREATE TABLE CartItem(
	id INT AUTO_INCREMENT,
	cart_id INT NOT NULL, 
    item_sku INT NOT NULL,
    qty INT NOT NULL,
    
    FOREIGN KEY (cart_id) REFERENCES Cart(id) ON DELETE CASCADE,
    FOREIGN KEY (item_sku) REFERENCES Item(sku) ON DELETE CASCADE,
    
    PRIMARY KEY (id)
    );
    

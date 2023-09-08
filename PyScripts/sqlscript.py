import subprocess


script = """
-- Creating database and selecting it
CREATE DATABASE webshop;
USE webshop;

-- ------------------------------------TABLES-----------------------------------

-- Table to hold customers
CREATE TABLE Customer (
    customer_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,
    f_name VARCHAR(50) NOT NULL,
    l_name VARCHAR(50) NOT NULL,
    street VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    zip VARCHAR(6) NOT NULL,
    phone VARCHAR(25) NOT NULL,
    email VARCHAR(50) NOT NULL
);

-- Table to display placed orders
CREATE TABLE Orders (
    order_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,
    customer_id INT UNSIGNED NOT NULL,
    order_date DATETIME NOT NULL,
    price INT UNSIGNED NOT NULL,
    status VARCHAR(30) DEFAULT 'Pending',
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

-- Products list
CREATE TABLE Product (
    product_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,
    brand VARCHAR(20) NOT NULL,
    product_name VARCHAR(50) NOT NULL,
    price INT UNSIGNED NOT NULL,
    quantity INT UNSIGNED NOT NULL
);

-- Product choosing for size and color variation
CREATE TABLE Product_choice (
    choice_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,
    product_id INT UNSIGNED NOT NULL,
    size VARCHAR(1) NOT NULL,
    color VARCHAR(20) NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);

-- Order Specs to links multiple products to an order
CREATE TABLE Order_Specs (
    spec_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,
    order_id INT UNSIGNED NOT NULL,
    product_id INT UNSIGNED NOT NULL,
    quantity INT UNSIGNED NOT NULL,
    choice_id INT UNSIGNED NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Product(product_id),
    FOREIGN KEY (choice_id) REFERENCES Product_choice(choice_id)
);

-- Table to show if an order has been shipped or not, serves no functional purpose
CREATE TABLE Shipment (
    shipment_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,
    order_id INT UNSIGNED NOT NULL,
    shipment_date DATETIME NOT NULL,
    street VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    zip VARCHAR(5) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);

-- List of all categories products can be associated with
CREATE TABLE Category (
    category_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,
    category_name VARCHAR(50) NOT NULL
);

-- CPR 'Category-Product Relation' actaully linking products with categories
CREATE TABLE CPR (
    cpr_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,
    product_id INT UNSIGNED NOT NULL,
    category_id INT UNSIGNED NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Product(product_id),
    FOREIGN KEY (category_id) REFERENCES Category(category_id)
);

-- -------------------------------------INSERTION--------------------------------------------


-- Street, city, phone allows separation. Ex. 'Main Street 123' - 'Mainstreet123' (Customer amount 20)
INSERT INTO customer (f_name, l_name, street, city, zip, phone, email)
VALUES
    ('John','Bernie','Main Street 123','New York','12345','+1 (555) 123-4567','main123@example.com'),
    ('Peter','Barker','Elm Street 45','Chicago','54321','+1 (555) 987-6543','elm45@example.com'),
    ('Johan','Karlsson','Drottninggatan 12','Stockholm','12345','+46 70 123 4567','drottning12@example.se'),
    ('Alice', 'Johnson', 'Maple Avenue 789', 'Los Angeles', '98765', '+1 (555) 234-5678', 'alice789@example.com'),
    ('David', 'Smith', 'Oak Drive 102', 'Houston', '21098', '+1 (555) 876-5432', 'david102@example.com'),
    ('Emily', 'Williams', 'Pine Street 67', 'San Francisco', '87654', '+1 (555) 345-6789', 'emily67@example.com'),
    ('Michael', 'Brown', 'Park Avenue 456', 'Miami', '34567', '+1 (555) 432-1098', 'michael456@example.com'),
    ('Sophia', 'Jones', 'Washington Boulevard 321', 'Seattle', '45678', '+1 (555) 987-6543', 'sophia321@example.com'),
    ('William', 'Davis', 'Lincoln Avenue 84', 'Phoenix', '32165', '+1 (555) 210-9876', 'william84@example.com'),
    ('Maria', 'Larsson', 'Strandvägen 7', 'Stockholm', '11123', '+46 70 987 6543', 'maria7@example.se'),
    ('Luis', 'Martinez', 'Calle de la Rosa 23', 'Madrid', '28001', '+34 612 345 678', 'luis23@example.es'),
    ('Elena', 'Kovacs', 'Andrassy ut 5', 'Budapest', '1061', '+36 30 987 6543', 'elena5@example.hu'),
    ('Sophie', 'Dubois', 'Rue de la Paix 9', 'Paris', '75002', '+33 6 78 12 34 56', 'sophie9@example.fr'),
    ('Hans', 'Muller', 'Hauptstrasse 55', 'Berlin', '10115', '+49 30 210 9876', 'hans55@example.de'),
    ('Giovanni', 'Rossi', 'Via Roma 13', 'Rome', '00187', '+39 333 456 7890', 'giovanni13@example.it'),
    ('Marta', 'González', 'Carrera 10 25-30', 'Barcelona', '08001', '+34 634 567 890', 'marta10@example.es'),
    ('Emma', 'Anderson', 'Birch Lane 30', 'London', '53748', '+44 20 1234 5678', 'emma30@example.co.uk'),
    ('Luca', 'Ferrari', 'Via Veneto 27', 'Milan', '20121', '+39 02 9876 5432', 'luca27@example.it'),
    ('Isabelle', 'Dubois', 'Rue de la Liberté 15', 'Paris', '75008', '+33 6 12 34 56 78', 'isabelle15@example.fr'),
    ('Antonio', 'López', 'Calle Gran Vía 40', 'Madrid', '28013', '+34 91 876 5432', 'antonio40@example.es');

    
-- Product name allows separation (Products 55)
INSERT INTO product (brand, product_name, price, quantity)
VALUES
    ('Adidas', 'Classic Cotton T-Shirt', 199, 23),
    ("Levi's", 'Slim Fit Denim Jeans', 499, 35),
    ('Nike', 'Sporty Hooded Sweatshirt', 299, 45),
    ('Puma', 'Running Sneakers', 399, 50),
    ('Zara', 'Elegant Summer Dress', 349, 10),
    ('Hugo Boss', 'Premium Formal Suit', 999, 5),
    ('Calvin Klein', 'Leather Biker Jacket', 799, 30),
    ('New Balance', 'Athletic Running Shoes', 449, 42),
    ('Lacoste', 'Polo Shirt Collection', 249, 21),
    ('H&M', 'Casual Cotton Shorts', 199, 11),                     -- 10
    ('The North Face', 'Warm Winter Coat', 899, 2),
    ('Mango', 'Chic Floral Print Skirt', 299, 36),
    ('Tommy Hilfiger', 'Cozy Knit Sweater', 399, 50),
    ('Ralph Lauren', 'Classic Checkered Blouse', 299, 50),
    ('Ecco', 'Genuine Leather Dress Shoes', 599, 47),
    ('Diesel', 'Vintage Denim Jacket', 549, 15),
    ('Ray-Ban', 'Stylish Sunglasses', 149, 17),
    ('Fjällräven', 'Durable Outdoor Backpack', 399, 25),
    ('Converse', 'Logo Baseball Cap', 129, 14),
    ('Guess', 'Leather Belt Collection', 199, 8),               -- 20
    ('Citizen', 'Elegant Wristwatch', 599, 4),
    ('Under Armour', 'Comfy Jogging Pants', 249, 12),
    ('Columbia', 'Warm Knit Beanie', 99, 32),
    ('Timberland', 'Outdoor Hiking Boots', 649, 50),
    ('Isotoner', 'Cozy Gloves Collection', 149, 50),
    ('Reebok', 'Sports Sweatpants', 299, 5),
    ('Tie Bar', 'Stylish Necktie Collection', 179, 18),
    ('Burberry', 'Classic Trench Coat', 799, 23),
    ('Carhartt', 'Logo Beanie', 129, 22),
    ('Cole Haan', 'Stylish Crossbody Bag', 349, 45),            -- 30
    ('Nike', 'Comfortable Socks (3-Pack)', 79, 28),
    ('UGG', 'Leather Gloves Collection', 199, 50),
    ('Fossil', 'Trendy Bracelet Collection', 99, 25),
    ('Columbia', 'Sun Hat Collection', 149, 45),
    ('Salomon', 'High-Performance Ski Jacket', 899, 34),
    ('Reebok', 'Gym Leggings Collection', 249, 26),
    ('The Sak', 'Shoulder Bag Collection', 399, 49),
    ('Outdoor Research', 'Warm Knit Scarf Collection', 149, 50),
    ('Brooks Brothers', 'Elegant Bow Tie Collection', 129, 50),
    ('Moose Knuckles', 'Faux Fur Coat Collection', 749, 5),         -- 40
    ('Dockers', 'Casual Cargo Pants', 299, 8),
    ('Kate Spade', 'Fashionable Earrings Collection', 99, 50),
    ('Patagonia', 'Outdoor Visor Collection', 129, 48),
    ("Arc'teryx", 'Lightweight Rain Jacket', 599, 23),
    ('Calvin Klein', "Men's Boxer Shorts (3-Pack)", 129, 20),
    ("Victoria's Secret", "Women's Silk Panties (5-Pack)", 199, 30),
    ('Nike', 'Comfortable Sneaker Socks (6-Pack)', 119, 35),
    ('Columbia', 'Versatile Bucket Hat Collection', 169, 50),
    ('Champion', 'Sporty Sweatband Set', 89, 50),
    ('Gap', 'Everyday Cotton T-Shirt Collection', 179, 50),         -- 50
    ('Wrangler', 'Slim Fit Denim Jeans Collection', 479, 47),
    ('Vans', 'Stylish Hooded Sweatshirt Collection', 279, 21),
    ('Superdry', 'Sneakers Collection', 369, 50),
    ('Forever 21', 'Charming Summer Dress Collection', 329, 50),
    ('Hollister', 'Elegant Formal Suit Collection', 899, 50);       -- 55
    

INSERT INTO category (category_name)
VALUES
    ('Fancy'), -- 1
    ('Footwear'), -- 2
    ('Bottom'), -- 3
    ('Top'), -- 4
    ('T-Shirt'), -- 5
    ('Underwear'), -- 6
    ('Jacket'), -- 7
    ('Accessories'), -- 8
    ('Sport'); -- 9
    
-- Associating products and categories, can have multiple
INSERT INTO cpr (product_id, category_id)
VALUES
    (1, 5),
    (2, 3),
    (3, 4),
    (4, 2),
    (4, 9),
    (5, 1),
    (6, 1),
    (7, 7),
    (8, 2),
    (8, 9),
    (9, 5),
    (10, 3),
    (11, 7),
    (12, 3),
    (13, 4),
    (14, 4),
    (15, 2),
    (16, 7),
    (17, 8),
    (18, 8),
    (19, 8),
    (20, 8),
    (21, 8),
    (22, 3),
    (22, 9),
    (23, 8),
    (24, 2),
    (25, 8),
    (26, 3),
    (26, 9),
    (27, 7),
    (28, 8),
    (29, 8),
    (30, 6),
    (31, 8),
    (32, 8),
    (33, 8),
    (34, 7),
    (35, 3),
    (35, 9),
    (36, 8),
    (37, 8),
    (38, 8),
    (39, 7),
    (39, 1),
    (40, 3),
    (41, 8),
    (42, 8),
    (43, 7),
    (44, 6),
    (45, 6),
    (46, 6),
    (47, 8),
    (48, 8),
    (48, 9),
    (49, 5),
    (50, 3),
    (51, 4),
    (52, 2),
    (53, 1),
    (54, 1);

    
-- ---------------------------------PROCEDURES-----------------------------------

-- Using delimiter to run the entire procedure as one block
DELIMITER //
CREATE PROCEDURE fill_product_choices(
    p_id INT UNSIGNED -- input variable when called
)
BEGIN
    -- Looping all products to fill size and color variation
    p_loop: LOOP
        IF p_id > 55 THEN
            LEAVE p_loop;
        END IF;
        INSERT INTO Product_choice (product_id, size, color)
        VALUES
            (p_id, 'M', 'Blue'),
            (p_id, 'M', 'Red'),
            (p_id, 'M', 'Yellow'),
            (p_id, 'M', 'White'),
            (p_id, 'M', 'Black'),
            (p_id, 'L', 'Blue'),
            (p_id, 'L', 'Red'),
            (p_id, 'L', 'Yellow'),
            (p_id, 'L', 'White'),
            (p_id, 'L', 'Black');
        SET p_id = p_id + 1;
    END LOOP p_loop;
END;
//
DELIMITER ;
CALL fill_product_choices(1);


DELIMITER //
-- Procedure takes input arguments to place order
-- When called 'CALL purchase (1,1,1,'M','Blue');'
CREATE PROCEDURE Purchase(
    purchase_customer_id INT UNSIGNED,
    purchase_product_id INT UNSIGNED,
    purchase_quantity INT UNSIGNED,
    purchase_size VARCHAR(1),
    purchase_color VARCHAR(20)
)
BEGIN
    -- Placeholder for price * quantity = amount_to_pay
    DECLARE amount_to_pay INT UNSIGNED;

    -- Declaring exit handler for sqlexception. If an exception is raise during
    -- the transaction below will will do a rollback of the code executed to then
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
    END;

    -- Getting price for placed order then checking if that equates to NULL
    -- If price is NULL there are no products
    IF (
        SELECT (price * purchase_quantity)
        FROM Product
        WHERE product_id = purchase_product_id
    ) IS NULL THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Out of order';
    END IF;

    -- Checking if placed order consists of more products than quantity of the product
    IF purchase_quantity > (
        SELECT quantity
        FROM Product
        WHERE product_id = purchase_product_id
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Not enough in stock';
    END IF;

    -- Starting transaction, execute all or nothing
    START TRANSACTION;

    -- Randomizing dates of placed orders for fictional data
    SET @start_date = '2021-01-01 00:00:00';
    SET @end_date = '2023-08-31 23:59:59';
    SET @random_date = DATE_ADD(@start_date, INTERVAL FLOOR(RAND() * TIMESTAMPDIFF(SECOND, @start_date, @end_date)) SECOND);
    
    -- Creating an order retriving the last updated order_id in session
    -- With DEFAULT NOW() from table 'orders' above randomization is not necessary
    INSERT INTO Orders (customer_id, order_date, price) VALUES (purchase_customer_id, @random_date, 0);
    SET @order_id = LAST_INSERT_ID();

    -- Filling order_specs with details of order, product and quantity
    INSERT INTO Order_Specs (order_id, product_id, quantity, choice_id)
    SELECT @order_id, purchase_product_id, purchase_quantity, pc.choice_id
    FROM Product_choice pc
    WHERE pc.product_id = purchase_product_id AND pc.size = purchase_size AND pc.color = purchase_color;

    -- Actual calculation for order price
    SELECT SUM(price * purchase_quantity) INTO amount_to_pay
    FROM Product
    WHERE product_id = purchase_product_id;

    -- Updating order, product with total price to pay and adjusting quantity in table
    UPDATE Orders
    SET price = amount_to_pay
    WHERE order_id = @order_id;

    UPDATE Product
    SET quantity = quantity - purchase_quantity
    WHERE product_id = purchase_product_id;
    COMMIT;
END;
//
DELIMITER ;


DELIMITER //
-- Procedure to fill in shipment information, taking customer_id input
CREATE PROCEDURE Ship (
    ship_customer_id INT UNSIGNED -- Ships all orders from a given customer with 'Pending' order status
)
BEGIN
    -- Retriving order_id and matching it aswell as retriving customer details
    INSERT INTO Shipment (order_id, shipment_date, street, city, zip)
    SELECT o.order_id, NOW(), c.street, c.city, c.zip
    FROM Orders o
    JOIN Customer c ON o.customer_id = c.customer_id
    WHERE o.customer_id = ship_customer_id AND o.status = 'Pending';
    
    -- Updating the status when order has been shipped
    UPDATE Orders
    SET status = 'Shipped'
    WHERE customer_id = ship_customer_id AND status = 'Pending';
    
END;
//
DELIMITER ;

-- ---------------------------FICTIONAL DATA PRODUCTION--------------------------------

DELIMITER //
CREATE PROCEDURE fill_purchases(
    c_increase INT UNSIGNED,
    p_increase INT UNSIGNED,
    q_increase INT UNSIGNED,
    size VARCHAR(1),
    color VARCHAR(20)
)
BEGIN
    DECLARE customer_id INT UNSIGNED DEFAULT 1;
    DECLARE product_id INT UNSIGNED DEFAULT 1;
    DECLARE quantity INT UNSIGNED DEFAULT 1;

    -- Default values set when called and loops until out of bounds
    -- Filling the database with mixed orders
    fp_loop: LOOP
        IF customer_id > 20 OR product_id > 55 OR quantity > 3 THEN
            LEAVE fp_loop;
        END IF;
        CALL purchase (customer_id,product_id,quantity,size,color);
        SET customer_id = customer_id + c_increase;
        SET product_id = product_id + p_increase;
        SET quantity = quantity + q_increase;
    END LOOP fp_loop;
END;
//
DELIMITER ;

-- Producing some results
CALL fill_purchases(5,5,0,'M','Black');
CALL fill_purchases(2,3,0,'L','Blue');
CALL fill_purchases(1,2,0,'M','Yellow');
CALL fill_purchases(4,8,0,'M','Red');
CALL fill_purchases(1,4,0,'L','White');

CALL ship(1);
CALL ship(11);
CALL ship(16);

"""


with open("temp_script.sql", "w") as file:
    file.write(script)

#.cnf file contains -u username -p password for mysql db
subprocess.run(["path/to/mysql.exe", "--defaults-file=path/to/.cnf", "<", "temp_script.sql"], shell=True)
subprocess.run(["del", "temp_script.sql"], shell=True)
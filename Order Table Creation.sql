create database funcdb

use funcdb

CREATE TABLE Orders (
    OrderID INT IDENTITY(1,1) PRIMARY KEY,
    OrderBy NVARCHAR(100) NOT NULL,
    OrderName NVARCHAR(100) NOT NULL,
    NumberOfItems INT NOT NULL,
    Cost DECIMAL(10, 2) NOT NULL,
    OrderDate DATETIME DEFAULT GETDATE()
);


INSERT INTO Orders (OrderBy, OrderName, NumberOfItems, Cost)
VALUES 
('Alice', 'Books', 3, 45.99),
('Bob', 'Laptop Accessories', 2, 89.50),
('Charlie', 'Office Furniture', 1, 299.99),
('David', 'Mobile Chargers', 5, 75.00),
('Eve', 'Stationery', 10, 25.00),
('Frank', 'Printer Ink', 4, 120.40),
('Grace', 'Software License', 1, 499.00),
('Hannah', 'Monitors', 2, 350.60),
('Ian', 'Keyboards', 3, 150.00),
('Jack', 'Mouse Pads', 8, 40.00),
('Karen', 'USB Cables', 12, 60.00),
('Leo', 'Desk Lamps', 6, 180.50),
('Mona', 'Headphones', 2, 220.99),
('Nina', 'Webcams', 3, 195.00),
('Oscar', 'Paper Reams', 20, 75.20),
('Paul', 'Filing Cabinets', 2, 250.00),
('Queen', 'Notebooks', 15, 90.75),
('Ryan', 'Hard Drives', 4, 320.00),
('Sophia', 'Power Banks', 5, 175.25),
('Tom', 'Bluetooth Speakers', 2, 130.80);

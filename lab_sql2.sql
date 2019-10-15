CREATE SCHEMA IF NOT EXISTS `lab_mysql2` DEFAULT CHARACTER SET utf8 ;
USE `lab_mysql2` ;

-- -----------------------------------------------------
-- Table `lab_mysql2`.`manufacturer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql2`.`manufacturer` (
  `id_manufacturer` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_manufacturer`))
ENGINE = MyISAM
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `lab_mysql22`.`cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql2`.`cars` (
  `id_cars` INT(11) NOT NULL AUTO_INCREMENT,
  `VIN` VARCHAR(45) NOT NULL,
  `model` VARCHAR(45) NOT NULL,
  `year` VARCHAR(45) NULL DEFAULT NULL,
  `color` ENUM('Blue', 'Red', 'White', 'silver', 'Gray') NOT NULL,
  `id_manufacturer` INT(11) NOT NULL,
  PRIMARY KEY (`id_cars`, `id_manufacturer`),
  INDEX `fk_cars_manufacturer1_idx` (`id_manufacturer` ASC))
ENGINE = MyISAM
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `lab_mysql2`.`customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql2`.`customers` (
  `id_cust` INT(11) NOT NULL AUTO_INCREMENT,
  `customer_id` INT(11) NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  `phone` VARCHAR(45) NULL DEFAULT NULL,
  `email` VARCHAR(50) NULL DEFAULT NULL,
  `address` VARCHAR(100) NOT NULL,
  `city` VARCHAR(50) NOT NULL,
  `state` VARCHAR(50) NOT NULL,
  `country` VARCHAR(50) NOT NULL,
  `zip` INT(30) NOT NULL,
  PRIMARY KEY (`id_cust`))
ENGINE = MyISAM
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `lab_mysql2`.`store`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql2`.`store` (
  `id_store` INT(11) NOT NULL AUTO_INCREMENT,
  `city` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id_store`))
ENGINE = MyISAM
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `lab_mysql2`.`salesperson`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql2`.`salesperson` (
  `id_salesperson` INT(11) NOT NULL AUTO_INCREMENT,
  `staff_id` INT(11) NOT NULL,
  `name` VARCHAR(100) NOT NULL,
  `id_store` INT(11) NOT NULL,
  PRIMARY KEY (`id_salesperson`, `id_store`),
  INDEX `fk_salesperson_store1_idx` (`id_store` ASC) )
ENGINE = MyISAM
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `lab_mysql2`.`invoices`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql2`.`invoices` (
  `id_invoice` INT(11) NOT NULL AUTO_INCREMENT,
  `invoice_number` INT(11) NOT NULL,
  `date` DATE NOT NULL,
  `id_cars` INT(11) NOT NULL,
  `id_customers` INT(11) NOT NULL,
  `id_salesperson` INT(11) NOT NULL,
  PRIMARY KEY (`id_invoice`, `id_cars`, `id_customers`, `id_salesperson`),
  INDEX `fk_invoices_cars_idx` (`id_cars` ASC) ,
  INDEX `fk_invoices_customers1_idx` (`id_customers` ASC) ,
  INDEX `fk_invoices_salesperson1_idx` (`id_salesperson` ASC) )
ENGINE = MyISAM
DEFAULT CHARACTER SET = utf8;
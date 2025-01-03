DROP TABLE IF EXISTS EMPRUNTER;
DROP TABLE IF EXISTS ECRIRE;
DROP TABLE IF EXISTS EMPRUNTEUR;
DROP TABLE IF EXISTS AUTEUR;
DROP TABLE IF EXISTS LIVRE;


-- Création des tables

CREATE TABLE LIVRE (
    ISBN VARCHAR(13) PRIMARY KEY NOT NULL,
    Titre VARCHAR(100) NOT NULL,
    Année_publication INT
);

CREATE TABLE AUTEUR (
    ID_Auteur INT PRIMARY KEY,
    Nom VARCHAR(50) NOT NULL,
    Prenom VARCHAR(50) NOT NULL
);

CREATE TABLE EMPRUNTEUR (
    ID_Emprunteur INT PRIMARY KEY,
    Nom VARCHAR(50) NOT NULL,
    Prenom VARCHAR(50) NOT NULL,
    Adresse VARCHAR(100) NOT NULL
);

CREATE TABLE ECRIRE (
    ISBN VARCHAR(13),
    ID_Auteur INT,
    PRIMARY KEY (ISBN, ID_Auteur),
    FOREIGN KEY (ISBN) REFERENCES LIVRE(ISBN),
    FOREIGN KEY (ID_Auteur) REFERENCES AUTEUR(ID_Auteur)
);

CREATE TABLE EMPRUNTER (
    ISBN VARCHAR(13),
    ID_Emprunteur INT,
    Date_emprunt DATE NOT NULL,
    PRIMARY KEY (ISBN, ID_Emprunteur),
    FOREIGN KEY (ISBN) REFERENCES LIVRE(ISBN),
    FOREIGN KEY (ID_Emprunteur) REFERENCES EMPRUNTEUR(ID_Emprunteur)
);

-- Insertion de données

INSERT INTO LIVRE (ISBN, Titre, Année_publication) VALUES
('9782070541270', 'Harry Potter à l''école des sorciers', 1997),
('9782070643028', 'Le Petit Prince', 1943),
('9782253151432', 'Les Misérables', 1862),
('9782070360024', '1984', 1949),
('9782070368228', 'Le Seigneur des Anneaux', 1954);

INSERT INTO AUTEUR (ID_Auteur, Nom, Prenom) VALUES
(1,'Rowling', 'J.K.'),
(2,'Saint-Exupéry', 'Antoine'),
(3,'Hugo', 'Victor'),
(4,'Orwell', 'George'),
(5,'Tolkien', 'J.R.R.');

INSERT INTO EMPRUNTEUR (ID_Emprunteur, Nom, Prenom, Adresse) VALUES
(1,'Dupont', 'Jean', '1 rue de la Paix, Paris'),
(2,'Martin', 'Sophie', '15 avenue des Champs-Élysées, Paris'),
(3,'Dubois', 'Pierre', '7 place Bellecour, Lyon'),
(4,'Lefebvre', 'Marie', '20 rue du Vieux Port, Marseille'),
(5,'Moreau', 'Éric', '3 rue du Taur, Toulouse');

INSERT INTO ECRIRE (ISBN, ID_Auteur) VALUES
('9782070541270', 1),
('9782070643028', 2),
('9782253151432', 3),
('9782070360024', 4),
('9782070368228', 5);

INSERT INTO EMPRUNTER (ISBN, ID_Emprunteur, Date_emprunt) VALUES
('9782070541270', 1, '2023-01-15'),
('9782070643028', 2, '2023-02-20'),
('9782253151432', 3, '2023-03-10'),
('9782070360024', 4, '2023-04-05'),
('9782070368228', 5, '2023-05-01');

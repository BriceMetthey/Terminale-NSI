DROP TABLE IF EXISTS PROGRAMMATION;
DROP TABLE IF EXISTS PARTICIPATION;
DROP TABLE IF EXISTS EQUIPEMENT;
DROP TABLE IF EXISTS INSCRIPTION;
DROP TABLE IF EXISTS ENSEIGNER;
DROP TABLE IF EXISTS CONCERT;
DROP TABLE IF EXISTS SALLE;
DROP TABLE IF EXISTS ELEVE;
DROP TABLE IF EXISTS PROFESSEUR;
DROP TABLE IF EXISTS COURS;


CREATE TABLE COURS (
    ID_Cours INT PRIMARY KEY,
    Nom VARCHAR(100) NOT NULL,
    Niveau VARCHAR(50),
    Tarif_horaire DECIMAL(10, 2)
);

CREATE TABLE PROFESSEUR (
    ID_Professeur INT PRIMARY KEY,
    Nom VARCHAR(50) NOT NULL,
    Prenom VARCHAR(50) NOT NULL,
    Instrument_principal VARCHAR(50),
    Telephone VARCHAR(20)
);

CREATE TABLE ELEVE (
    ID_Eleve INT PRIMARY KEY,
    Nom VARCHAR(50) NOT NULL,
    Prenom VARCHAR(50) NOT NULL,
    Date_naissance DATE,
    Email VARCHAR(100)
);

CREATE TABLE SALLE (
    Numero_salle INT PRIMARY KEY,
    Capacite INT
);

CREATE TABLE CONCERT (
    ID_Concert INT PRIMARY KEY,
    Date DATE,
    Lieu VARCHAR(100),
    Titre VARCHAR(200)
);

CREATE TABLE ENSEIGNER (
    ID_Professeur INT,
    ID_Cours INT,
    PRIMARY KEY (ID_Professeur, ID_Cours),
    FOREIGN KEY (ID_Professeur) REFERENCES PROFESSEUR(ID_Professeur),
    FOREIGN KEY (ID_Cours) REFERENCES COURS(ID_Cours)
);

CREATE TABLE INSCRIPTION (
    ID_Eleve INT,
    ID_Cours INT,
    Date_inscription DATE,
    PRIMARY KEY (ID_Eleve, ID_Cours),
    FOREIGN KEY (ID_Eleve) REFERENCES ELEVE(ID_Eleve),
    FOREIGN KEY (ID_Cours) REFERENCES COURS(ID_Cours)
);

CREATE TABLE EQUIPEMENT (
    ID_Equipement INT PRIMARY KEY,
    Numero_salle INT,
    Type_instrument VARCHAR(50),
    FOREIGN KEY (Numero_salle) REFERENCES SALLE(Numero_salle)
);

CREATE TABLE PARTICIPATION (
    ID_Eleve INT,
    ID_Concert INT,
    Morceau_joue VARCHAR(100),
    PRIMARY KEY (ID_Eleve, ID_Concert),
    FOREIGN KEY (ID_Eleve) REFERENCES ELEVE(ID_Eleve),
    FOREIGN KEY (ID_Concert) REFERENCES CONCERT(ID_Concert)
);

CREATE TABLE PROGRAMMATION (
    ID_Cours INT,
    Numero_salle INT,
    Jour DATE,
    Heure_debut TIME,
    Heure_fin TIME,
    PRIMARY KEY (ID_Cours, Numero_salle),
    FOREIGN KEY (ID_Cours) REFERENCES COURS(ID_Cours),
    FOREIGN KEY (Numero_salle) REFERENCES SALLE(Numero_salle)
);



-- Insertion dans la table COURS
INSERT INTO COURS (ID_Cours, Nom, Niveau, Tarif_horaire) VALUES
(1, 'Piano débutant', 'Débutant', 30.00),
(2, 'Guitare intermédiaire', 'Intermédiaire', 35.00),
(3, 'Chant avancé', 'Avancé', 40.00);

-- Insertion dans la table PROFESSEUR
INSERT INTO PROFESSEUR (ID_Professeur, Nom, Prenom, Instrument_principal, Telephone) VALUES
(1, 'Dupont', 'Jean', 'Piano', '0123456789'),
(2, 'Martin', 'Sophie', 'Guitare', '0987654321');

-- Insertion dans la table ELEVE
INSERT INTO ELEVE (ID_Eleve, Nom, Prenom, Date_naissance, Email) VALUES
(1, 'Dubois', 'Marie', '2000-05-15', 'marie.dubois@email.com'),
(2, 'Lefebvre', 'Pierre', '1995-11-30', 'pierre.lefebvre@email.com');

-- Insertion dans la table SALLE
INSERT INTO SALLE (Numero_salle, Capacite) VALUES
(101, 20),
(102, 15);

-- Insertion dans la table CONCERT
INSERT INTO CONCERT (ID_Concert, Date, Lieu, Titre) VALUES
(1, '2025-06-15', 'Salle des fêtes', 'Concert de fin d''année');

-- Insertion dans la table ENSEIGNER
INSERT INTO ENSEIGNER (ID_Professeur, ID_Cours) VALUES
(1, 1),
(2, 2);

-- Insertion dans la table INSCRIPTION
INSERT INTO INSCRIPTION (ID_Eleve, ID_Cours, Date_inscription) VALUES
(1, 1, '2024-09-01'),
(2, 2, '2024-09-02');

-- Insertion dans la table EQUIPEMENT
INSERT INTO EQUIPEMENT (ID_Equipement, Numero_salle, Type_instrument) VALUES
(1, 101, 'Piano'),
(2, 102, 'Guitare');

-- Insertion dans la table PARTICIPATION
INSERT INTO PARTICIPATION (ID_Eleve, ID_Concert, Morceau_joue) VALUES
(1, 1, 'Sonate au clair de lune'),
(2, 1, 'Stairway to Heaven');

-- Insertion dans la table PROGRAMMATION
INSERT INTO PROGRAMMATION (ID_Cours, Numero_salle, Jour, Heure_debut, Heure_fin) VALUES
(1, 101, '2022-05-15', '14:00', '15:30'),
(2, 102, '2023-07-10', '16:00', '17:30');


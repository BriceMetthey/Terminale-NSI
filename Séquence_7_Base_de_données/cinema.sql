-- Supprimer les tables dans l'ordre inverse de leur création
DROP TABLE IF EXISTS RESERVATION;
DROP TABLE IF EXISTS REALISER;
DROP TABLE IF EXISTS SEANCE;
DROP TABLE IF EXISTS CLIENT;
DROP TABLE IF EXISTS FILM;
DROP TABLE IF EXISTS REALISATEUR;
DROP TABLE IF EXISTS SALLE;


-- Création des tables

CREATE TABLE SALLE (
    Numero_salle INT PRIMARY KEY,
    Capacite INT NOT NULL CHECK (Capacite > 0),
    Type_ecran VARCHAR(50) NOT NULL
);

CREATE TABLE FILM (
    Code_film INT PRIMARY KEY,
    Titre VARCHAR(100) NOT NULL,
    Duree INT NOT NULL CHECK (Duree > 0),
    Annee_sortie INT NOT NULL,
    Classification VARCHAR(50)
);

CREATE TABLE REALISATEUR (
    ID_realisateur INT PRIMARY KEY,
    Nom VARCHAR(50) NOT NULL,
    Prenom VARCHAR(50) NOT NULL
);

CREATE TABLE SEANCE (
    ID_seance INT PRIMARY KEY,
    Date DATE NOT NULL,
    Heure_debut TIME NOT NULL,
    Code_film INT,
    Numero_salle INT,
    FOREIGN KEY (Code_film) REFERENCES FILM(Code_film),
    FOREIGN KEY (Numero_salle) REFERENCES SALLE(Numero_salle)
);

CREATE TABLE CLIENT (
    Numero_client INT PRIMARY KEY,
    Nom VARCHAR(50) NOT NULL,
    Prenom VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE
);

CREATE TABLE REALISER (
    Code_film INT,
    ID_realisateur INT,
    PRIMARY KEY (Code_film, ID_realisateur),
    FOREIGN KEY (Code_film) REFERENCES FILM(Code_film),
    FOREIGN KEY (ID_realisateur) REFERENCES REALISATEUR(ID_realisateur)
);

CREATE TABLE RESERVATION (
    Numero_client INT,
    ID_seance INT,
    Nombre_places INT NOT NULL CHECK (Nombre_places > 0),
    PRIMARY KEY (Numero_client, ID_seance),
    FOREIGN KEY (Numero_client) REFERENCES CLIENT(Numero_client),
    FOREIGN KEY (ID_seance) REFERENCES SEANCE(ID_seance)
);

-- Insertion de données

INSERT INTO SALLE (Numero_salle, Capacite, Type_ecran) VALUES
(1, 100, '2D'),
(2, 150, '3D'),
(3, 200, 'IMAX');

INSERT INTO FILM (Code_film, Titre, Duree, Annee_sortie, Classification) VALUES
(1, 'Inception', 148, 2010, 'Tous publics'),
(2, 'The Dark Knight', 152, 2008, 'Tous publics'),
(3, 'Interstellar', 169, 2014, 'Tous publics');

INSERT INTO REALISATEUR (ID_realisateur, Nom, Prenom) VALUES
(1, 'Nolan', 'Christopher'),
(2, 'Spielberg', 'Steven'),
(3, 'Scorsese', 'Martin');

INSERT INTO SEANCE (ID_seance, Date, Heure_debut, Code_film, Numero_salle) VALUES
(1, '2023-12-15', '14:00:00', 1, 1),
(2, '2023-12-15', '17:00:00', 2, 2),
(3, '2023-12-16', '20:00:00', 3, 3);

INSERT INTO CLIENT (Numero_client, Nom, Prenom, Email) VALUES
(1, 'Dupont', 'Jean', 'jean.dupont@email.com'),
(2, 'Martin', 'Sophie', 'sophie.martin@email.com'),
(3, 'Dubois', 'Pierre', 'pierre.dubois@email.com');

INSERT INTO REALISER (Code_film, ID_realisateur) VALUES
(1, 1),
(2, 1),
(3, 1);

INSERT INTO RESERVATION (Numero_client, ID_seance, Nombre_places) VALUES
(1, 1, 2),
(2, 2, 3),
(3, 3, 1);

sudo apt update
sudo apt install postgresql postgresql-contrib -y
sudo service postgresql start
sudo -i -u postgres
psql

CREATE DATABASE hospital_db;
\c hospital_db;

CREATE TABLE Doctors (
    DoctorID SERIAL PRIMARY KEY,
    Name VARCHAR(100),
    Specialization VARCHAR(100),
    Experience INT
);

CREATE TABLE Patients (
    PatientID SERIAL PRIMARY KEY,
    Name VARCHAR(100),
    Age INT,
    Gender VARCHAR(10),
    AdmissionDate DATE,
    DoctorID INT REFERENCES Doctors(DoctorID)
);

INSERT INTO Doctors (Name, Specialization, Experience) VALUES
('Dr. Sharma', 'Cardiology', 10),
('Dr. Mehta', 'Neurology', 8),
('Dr. Rao', 'Cardiology', 15);

INSERT INTO Patients (Name, Age, Gender, AdmissionDate, DoctorID) VALUES
('Amit', 25, 'Male', '2024-06-15', 1),
('Sneha', 40, 'Female', '2024-06-15', 2),
('Raj', 60, 'Male', '2024-06-14', 1),
('Priya', 30, 'Female', '2024-06-13', 3);

SELECT * FROM Patients;

SELECT * 
FROM Patients
WHERE AdmissionDate = '2024-06-15';

SELECT 
    CASE 
        WHEN Age < 18 THEN 'Child'
        WHEN Age BETWEEN 18 AND 60 THEN 'Adult'
        ELSE 'Senior'
    END AS AgeGroup,
    COUNT(*) AS TotalPatients
FROM Patients
GROUP BY AgeGroup;

UPDATE Patients
SET Name = 'Rahul'
WHERE PatientID = 1;

SELECT *
FROM Doctors
WHERE Specialization = 'Cardiology';

SELECT d.Name AS DoctorName, COUNT(p.PatientID) AS TotalPatients
FROM Doctors d
LEFT JOIN Patients p ON d.DoctorID = p.DoctorID
GROUP BY d.Name;

SELECT AVG(Experience) AS AvgExperience
FROM Doctors;

\q
exit

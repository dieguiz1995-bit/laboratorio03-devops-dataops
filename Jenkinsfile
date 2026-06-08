pipeline {
    agent any
    stages {
        stage('Validar Python') {
            steps {
                bat '"C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" --version'
            }
        }
        stage('Instalar dependencias') {
            steps {
                bat '"C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install pandas'
            }
        }
        stage('Ejecutar procesamiento') {
            steps {
                bat '"C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" scripts\\procesamiento.py'
            }
        }
        stage('Validacion final') {
            steps {
                echo 'Pipeline ejecutado correctamente'
            }
        }

    }
}
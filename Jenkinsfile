// Definición de un Pipeline Declarativo en Jenkins
pipeline {
    // Define dónde se ejecutará el pipeline.
    // 'any' significa que se ejecutará en cualquier agente (máquina) disponible.
    // Puedes especificar un agente particular con una etiqueta, por ejemplo: agent { label 'my-agent' }
    agent any

    // Variables de entorno que estarán disponibles en todas las etapas.
    // Puedes añadir más si son necesarias para tu build.
    // environment {
    //     VERSION_APP = '1.0.0'
    // }

    // Define las diferentes etapas del pipeline.
    stages {

        // Etapa para obtener el código fuente del repositorio.
        // Jenkins a menudo hace esto automáticamente si el pipeline está configurado
        // para ejecutarse desde SCM, pero es buena práctica tener la etapa explícita.
        stage('Checkout') {
            steps {
                echo 'Clonando/Obteniendo el código del repositorio...'
                // El paso 'checkout scm' es el que realmente obtiene el código.
                // Se ejecuta automáticamente si configuras el job como Pipeline from SCM,
                // pero lo ponemos explícito aquí para claridad.
                checkout scm
            }
        }

        // Etapa para instalar las dependencias del proyecto.
        stage('Instalar dependencias') {
            steps {
                echo 'Instalando dependencias (del requirements.txt)...'
                // Ejecuta el comando pip para instalar las dependencias.
                // Asegúrate de que el agente tenga Python y pip instalados.
                bat '"C:\\Users\\User A1\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Verificar PATH') {
            steps {
                echo 'Verificando la variable PATH...'
                bat 'echo %PATH%'
            }
        }
        
        // Etapa para realizar análisis de código estático (linting).
        // Ayuda a mantener la calidad y el estilo del código.
        stage('Linting') {
            steps {
                echo 'Ejecutando análisis de código con flake8...'
                // Ejecuta flake8 (asumiendo que está en requirements.txt o instalado).
                // El punto '.' indica que analice el directorio actual.
                // Puedes añadir opciones como --max-line-length=120 etc.
                bat """
                       dir
                       echo "---"
                       "C:\\\\Users\\\\User A1\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python313\\\\python.exe" -m flake8 APP"
                """
            }
        }

        // Etapa para construir el proyecto (si aplica).
        // Para Python, esto podría ser crear un paquete, una imagen Docker, etc.
        // Aquí solo simula la acción.
        stage('Build') {
            steps {
                echo 'Simulando construcción o empaquetado del proyecto Python...'
                // Aquí irían los pasos reales para generar tu "artefacto" si lo hubiera, por ejemplo:
                // sh 'python setup.py sdist bdist_wheel' // Si usas setup.py
                // sh 'docker build -t mi-app-python:latest .' // Si construyes una imagen Docker
            }
        }

        // Etapa para ejecutar las pruebas unitarias y de integración.
        stage('Test') {
            steps {
                script {
                    env.PYTHONPATH = "${WORKSPACE}"
                    echo "PYTHONPATH is: ${env.PYTHONPATH}"
                    bat "cd ${WORKSPACE}" // Cambia el directorio de trabajo a la raíz
                    bat "\"C:\\\\Users\\\\User A1\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python313\\\\python.exe\" -m pytest --junitxml report.xml TESTS\""
                }
            }
            post {
                always {
                    echo 'Archivando resultados de pruebas...'
                    junit 'report.xml'
                    archiveArtifacts artifacts: 'report.xml', fingerprint: true, allowEmptyArchive: true
                }
            }
        }

        // Etapa para desplegar la aplicación.
        // Esta etapa es típicamente condicional. Aquí la hacemos para la rama 'main'.
        stage('Deploy') {
            // Solo ejecuta esta etapa si la rama actual es 'main'.
            when {
                branch 'main'
            }
            steps {
                echo 'Realizando despliegue a entorno de prueba (simulado)...'
                // Aquí irían los comandos REALES para desplegar tu aplicación.
                // Por ejemplo:
                // sh 'ssh user@tu_servidor "systemctl restart mi-app"' // Reiniciar un servicio
                // sh 'docker-compose up -d' // Levantar contenedores Docker
                // sh './scripts/deploy_to_staging.sh' // Ejecutar un script de despliegue
                echo 'Despliegue simulado completado.'
            }
        }
    }

    // Acciones que se ejecutan después de que todas las etapas del pipeline han finalizado.
    post {
        // Bloque que se ejecuta si el pipeline completó todas sus etapas con éxito.
        success {
            echo '✅ Pipeline finalizado con éxito.'
            // Aquí puedes añadir notificaciones de éxito (correo, Slack, etc.)
            slackSend channel: '#todo-uggrupo-c', message: "El pipeline fue ejecutado sin problemas. Build: ${env.BUILD_NUMBER}", teamDomain: 'uggrupoc', tokenCredentialId: 'slack1'
        }
        // Bloque que se ejecuta si el pipeline falló en alguna etapa.
        failure {
            echo '❌ Pipeline fallido.'
            // Aquí puedes añadir notificaciones de fallo (correo, Slack, etc.)
            slackSend channel: '#todo-uggrupo-c', message: "¡ERROR! El pipeline ha fallado. Build: ${env.BUILD_NUMBER}. Revisa Jenkins: ${env.BUILD_URL}", teamDomain: 'uggrupoc', tokenCredentialId: 'slack1'
        }
        // Bloque que se ejecuta siempre, sin importar el resultado (éxito, fallo, abortado).
        always {
            echo 'Limpiando espacio de trabajo...'
            // Limpia el directorio de trabajo del agente al finalizar.
            deleteDir()
            echo 'Fin del Pipeline.'
        }
    }
}

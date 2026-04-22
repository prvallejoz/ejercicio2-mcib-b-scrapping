<img width="1359" height="714" alt="image" src="https://github.com/user-attachments/assets/0b38a7b0-758e-43ed-a42b-d163d05acfd4" />Tratamiento de Datos Ejercicio - Consulta de Matrículas ANT con Selenium

Para el desarrollo del presente ejercicio se plantea la automatización de la consulta de valores de matrícula vehicular en el portal de la Agencia Nacional de Tránsito del Ecuador Agencia Nacional de Tránsito. El objetivo es procesar múltiples placas vehiculares almacenadas en un archivo Excel y obtener información detallada de cada una mediante técnicas de web scraping automatizado.

El sistema toma como entrada un archivo llamado PLACAS.xlsx, el cual contiene una lista de placas vehiculares. A partir de estos datos, se realiza la consulta en línea en el sitio oficial de la ANT:
https://ant.com.ec/matriculas/consultar-valor-matricula

Para la automatización del navegador se utiliza la librería Selenium junto con ChromeDriver, permitiendo simular la interacción de un usuario real en el sitio web. Esto incluye el ingreso de la placa, el envío del formulario y la extracción de los resultados mostrados en pantalla.

Como primer paso, el sistema lee el archivo Excel utilizando la librería pandas, recorriendo cada fila para obtener el valor de la placa a consultar.

<img width="1359" height="714" alt="image" src="https://github.com/user-attachments/assets/538742d2-adae-41f9-957c-45c656260d89" />

Posteriormente, por cada placa se abre una instancia del navegador, se accede al portal de la ANT y se realiza la búsqueda correspondiente. En caso de que la placa no exista o sea inválida, el sistema detecta la alerta emergente y registra valores por defecto como "NO EXISTE".

<img width="1359" height="767" alt="image" src="https://github.com/user-attachments/assets/cf91dd4f-297d-4425-b52f-6dd4ac98b546" />

<img width="1359" height="767" alt="image" src="https://github.com/user-attachments/assets/262b7d6e-1bc3-4319-b386-beb30a5dc05a" />

<img width="1359" height="767" alt="image" src="https://github.com/user-attachments/assets/53f98277-893a-46b7-9351-356d40300ac0" />

Cuando la consulta es exitosa, el sistema extrae información relevante del vehículo, incluyendo:

Marca
Modelo
Año del modelo
País de origen
Cantón
Clase y servicio
Cilindraje
Fechas importantes (caducidad, última revisión, compra, matrícula)
Total a pagar

<img width="1064" height="673" alt="image" src="https://github.com/user-attachments/assets/03b5d9c6-e152-4b0b-84c3-717693121f44" />

En caso de errores durante la ejecución (por ejemplo, fallos en la carga de la página o problemas de conexión), el sistema captura una imagen del error (screenshot) para facilitar la depuración y registra los datos con el estado "ERROR".

<img width="1359" height="767" alt="image" src="https://github.com/user-attachments/assets/de62ace0-9ab0-4811-9b2a-f70f59523be7" />

Finalmente, todos los resultados obtenidos son almacenados en un archivo resultados.csv, permitiendo su posterior análisis o procesamiento.

Captura de pantalla resultados

<img width="1359" height="767" alt="image" src="https://github.com/user-attachments/assets/a2b22618-ec32-4744-ab01-aa9be2ae4d4f" />

Adicionalmente, se implementa un control de tiempos de espera entre consultas para evitar bloqueos del sitio web y simular un comportamiento más humano durante la navegación automatizada.

<img width="543" height="168" alt="image" src="https://github.com/user-attachments/assets/84068de1-2a80-46f9-a753-040389551c0d" />

Consideraciones
Es necesario contar con Google Chrome instalado.
El sistema descarga automáticamente el driver correspondiente mediante webdriver_manager, para esto es necesario que se cuente con acceso a internet.
El archivo PLACAS.xlsx debe estar en la misma ruta del script.
Se recomienda no ejecutar consultas masivas en corto tiempo para evitar restricciones del sitio web.

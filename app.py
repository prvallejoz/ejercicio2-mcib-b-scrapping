from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

archivo = "C:/Users/bryan/Downloads/PLACAS.xlsx"
df = pd.read_excel(archivo, header=None)

resultados = []

for index, row in df.iterrows():

    valor = str(row[0]).strip().upper()
    print(f"Consultando: {valor}")

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    wait = WebDriverWait(driver, 20)

    try:
        driver.get("https://ant.com.ec/matriculas/consultar-valor-matricula")

        input_placa = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='MNA0123']"))
        )
        input_placa.clear()
        input_placa.send_keys(valor)

        driver.find_element(By.XPATH, "//button[contains(., 'Consultar')]").click()

        time.sleep(5)

        if driver.find_elements(By.CLASS_NAME, "swal2-popup"):
            print(f"Placa inválida: {valor}")

            driver.find_element(By.XPATH, "//button[contains(., 'Aceptar')]").click()

            resultados.append({
                "placa": valor,
                "anio_pago": "NO EXISTE",
                "marca": "NO EXISTE",
                "modelo": "NO EXISTE",
                "anio_modelo": "NO EXISTE",
                "pais": "NO EXISTE",
                "ramv": "NO EXISTE",
                "canton": "NO EXISTE",
                "clase": "NO EXISTE",
                "servicio": "NO EXISTE",
                "cilindraje": "NO EXISTE",
                "fecha_caducidad": "NO EXISTE",
                "fecha_ultima": "NO EXISTE",
                "fecha_compra": "NO EXISTE",
                "fecha_matricula": "NO EXISTE",
                "total_pagar": "NO EXISTE"
            })

            driver.quit()
            continue

        if not driver.find_elements(By.CSS_SELECTOR, "div.card.my-4"):
            print(f"No cargó resultado para: {valor}")

            driver.save_screenshot(f"error_{valor}.png")

            driver.quit()
            continue

        contenedor = driver.find_element(By.CSS_SELECTOR, "div.card.my-4")

        placa = contenedor.find_element(By.XPATH, ".//b[text()='Placa']/following::p[1]").text
        anio = contenedor.find_element(By.XPATH, ".//b[contains(text(),'Último año')]/following::p[1]").text
        tablas = contenedor.find_elements(By.TAG_NAME, "table")
        tabla1 = tablas[0].find_elements(By.TAG_NAME, "td") if len(tablas) > 0 else []
        marca = tabla1[0].text if len(tabla1) > 0 else ""
        modelo = tabla1[1].text if len(tabla1) > 1 else ""
        anio_modelo = tabla1[2].text if len(tabla1) > 2 else ""
        pais = tabla1[3].text if len(tabla1) > 3 else ""
        
        tabla2 = tablas[1].find_elements(By.TAG_NAME, "td") if len(tablas) > 1 else []
        ramv = tabla2[0].text if len(tabla2) > 0 else ""
        canton = tabla2[1].text if len(tabla2) > 1 else ""
        clase = tabla2[2].text if len(tabla2) > 2 else ""
        servicio = tabla2[3].text if len(tabla2) > 3 else ""
        cilindraje = tabla2[4].text if len(tabla2) > 4 else ""

        tabla3 = tablas[2].find_elements(By.TAG_NAME, "td") if len(tablas) > 2 else []
        fecha_caducidad = tabla3[0].text if len(tabla3) > 0 else ""
        fecha_ultima = tabla3[1].text if len(tabla3) > 1 else ""
        fecha_compra = tabla3[2].text if len(tabla3) > 2 else ""
        fecha_matricula = tabla3[3].text if len(tabla3) > 3 else ""

        total = contenedor.find_element(By.XPATH, ".//b[contains(text(),'USD')]").text

        resultados.append({
            "placa": placa,
            "anio_pago": anio,

            "marca": marca,
            "modelo": modelo,
            "anio_modelo": anio_modelo,
            "pais": pais,

            "ramv": ramv,
            "canton": canton,
            "clase": clase,
            "servicio": servicio,
            "cilindraje": cilindraje,

            "fecha_caducidad": fecha_caducidad,
            "fecha_ultima": fecha_ultima,
            "fecha_compra": fecha_compra,
            "fecha_matricula": fecha_matricula,

            "total_pagar": total
        })

    except Exception as e:
        print(f"Error con {valor}: {type(e).__name__} - {e}")

        driver.save_screenshot(f"error_{valor}.png")

        resultados.append({
            "placa": valor,
            "anio_pago": "ERROR",
            "marca": "ERROR",
            "modelo": "ERROR",
            "anio_modelo": "ERROR",
            "pais": "ERROR",
            "ramv": "ERROR",
            "canton": "ERROR",
            "clase": "ERROR",
            "servicio": "ERROR",
            "cilindraje": "ERROR",
            "fecha_caducidad": "ERROR",
            "fecha_ultima": "ERROR",
            "fecha_compra": "ERROR",
            "fecha_matricula": "ERROR",
            "total_pagar": "ERROR"
        })

    driver.quit()

    time.sleep(4)

df_final = pd.DataFrame(resultados)
print(df_final)

df_final.to_csv("resultados_test.csv", index=False)
import streamlit as st
from PIL import Image, ImageOps, ImageDraw

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Portfolio de Fran",
    page_icon="📊",
    layout="wide"
)

# --- OCULTAR ELEMENTOS DE LA INTERFAZ ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- FUNCIÓN PARA RECORTAR IMAGEN CIRCULAR ---
def crear_imagen_circular(imagen_path):
    img = Image.open(imagen_path)
    # Convertimos para asegurar compatibilidad
    img = img.convert("RGBA") 
    
    # Preparamos la máscara circular
    bigsize = (img.size[0] * 3, img.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask) 
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(img.size, Image.Resampling.LANCZOS)
    
    # Aplicamos la máscara
    img.putalpha(mask)
    return img

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    # Si tenés una foto, descomentá la siguiente línea y poné el nombre del archivo
    imagen_circular = crear_imagen_circular("Foto_Mia.jpg") 
    st.image(imagen_circular, width=150)
    
    st.title("Francisco Peix")
    st.caption("Data Science Student @ UBA")
    
    st.write("---")
    
    # Menú de navegación
    seccion = st.radio("Ir a:", ["Sobre Mí", "Proyectos", "Habilidades", "Contacto"])
    
    st.write("---")

    st.markdown("### Enlaces")
    st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/francisco-peix-1884092a8)")
    st.markdown("🐙 [GitHub](https://github.com/franpeix)")

# --- BOTÓN DE DESCARGA DE CV ---
# Para que funcione, tenés que poner tu archivo PDF en la misma carpeta
st.link_button("📄 Descargar mi CV", "https://drive.google.com/file/d/1qiMh6Zk--kHo3uoHwp9MQjBfBiGXmz8I/view?usp=sharing")

# --- SECCIÓN: SOBRE MÍ ---
if seccion == "Sobre Mí": # Asegurate que este texto coincida con tu menú lateral
    st.title("Perfil Profesional 👨‍💻")

    # 1. LOS NÚMEROS QUE VENDEN (KPIs)
    # Usamos columnas para mostrar métricas grandes. Esto impacta visualmente.
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Promedio UBA", value="9.50", delta="Excelencia Académica")
    with col2:
        st.metric(label="Título Intermedio", value="Bachiller", delta="Ciencias de Datos")
    with col3:
        st.metric(label="Estado de Carrera", value="Avanzado", delta="Licenciatura")

    st.write("---") # Línea separadora

    # 2. TU BIO (La versión pulida que armamos para LinkedIn)
    st.subheader("Bio")
    
    # Dividimos en dos columnas: Texto a la izquierda, Datos clave a la derecha
    col_bio, col_detalles = st.columns([2, 1])
    
    with col_bio:
        st.markdown("""
        Estudiante de **Ciencia de Datos en la UBA (Exactas)**. Mi formación combina la rigurosidad matemática 
        (Probabilidad, Estadística) con la capacidad práctica de resolver problemas de negocio.

        🚀 **Mi Enfoque:**
        Disfruto todo el ciclo del dato: desde la limpieza (ETL) y el análisis exploratorio, hasta el modelado predictivo 
        y la visualización. Me interesan especialmente los desafíos en **Finanzas, Salud y Tecnología**.

        🏃‍♂️ **Dato Personal:**
        Llevo la disciplina del deporte (running y gimnasio) a mi vida profesional: creo firmemente en la constancia 
        y la mejora continua.
        """)

    with col_detalles:
        st.info("💡 **Intereses**")
        st.markdown("""
        - 📈 Finanzas e Inversiones
        - 🏥 Salud y Deporte
        - 🤖 Automatización de Tareas
        - 📊 Visualización de Datos
        """)
        
        st.success("🎓 **Educación**")
        st.markdown("**Univ. de Buenos Aires**\n*Lic. en Cs. de Datos*")

# --- SECCIÓN: PROYECTOS ---
elif seccion == "Proyectos":
    st.title("Proyectos Académicos 🚀")
    st.markdown("Un recorrido por mis trabajos prácticos más relevantes en la Licenciatura.")

    # Pestañas para navegar entre proyectos
    tab1, tab2, tab3 = st.tabs(["Clasificación de Imágenes (MNIST-C)", "Red de Museos (Grafos)", "Análisis de Datos Nacionales"])

    # --- PROYECTO 1: MNIST (Inteligencia Artificial) ---
    with tab1:
        st.header("Clasificación de Imágenes con Ruido (MNIST-C)")
        st.caption("🛠️ Stack: Python | Scikit-Learn | KNN | Árboles de Decisión")
        
        col_text, col_code = st.columns([1, 1.3]) # Izquierda (Texto+Img) / Derecha (Código)
        
        with col_text:
            # 1. IMAGEN (Evidencia)
            try:
                st.image("MNIST_C.jpeg", caption="Muestra del dataset corrupto (MNIST-C)", use_container_width=True)
            except FileNotFoundError:
                st.info("📷 (Acá iría la imagen 'MNIST_C.jpeg')")

            st.divider()

            # 2. EXPLICACIÓN
            st.markdown("""
            **📌 El Problema:**
            El dataset MNIST (dígitos escritos a mano) es trivial, pero ¿qué pasa cuando las imágenes tienen "niebla" o ruido?
            
            **💡 Mi Solución:**
            Evalué y comparé modelos de **Árboles de Decisión** vs. **K-Nearest Neighbors (KNN)**.
            
            **🚀 Resultados:**
            * Detecté que KNN maneja mejor el ruido local que los árboles.
            * Implementé optimización de hiperparámetros para mejorar la precisión.
            """)
        
        with col_code:
            st.markdown("📄 **Snippet de mi Código:**")
            st.code('''
from sklearn.neighbors import KNeighborsClassifier

# Configuración del modelo KNN para resistir ruido
# Usamos 'distance' para dar más peso a vecinos cercanos
knn = KNeighborsClassifier(n_neighbors=5, weights='distance')

# Entrenamiento con datos corruptos
knn.fit(X_train_corrupto, y_train)

# Evaluación
score = knn.score(X_test, y_test)
print(f"Precisión del modelo: {score:.2%}")
            ''', language='python')

    # --- PROYECTO 2: MUSEOS (Grafos) ---
    with tab2:
        st.header("Análisis de Conectividad: Museos de CABA")
        st.caption("🛠️ Stack: Python | NetworkX | Geopandas | Matplotlib")
        
        col_text, col_code = st.columns([1, 1.3])
        
        with col_text:
            # 1. IMAGEN
            try:
                st.image("RedMuseos.png", caption="Visualización del Grafo de Museos", use_container_width=True)
            except FileNotFoundError:
                st.info("📷 (Acá iría la imagen 'RedMuseos.png')")

            st.divider()

            # 2. EXPLICACIÓN
            st.markdown("""
            **📌 El Objetivo:**
            Modelar la red de museos de la Ciudad de Buenos Aires para entender su conectividad y potencial turístico.
            
            **💡 Metodología:**
            Utilicé **Teoría de Grafos**. Los nodos son los museos y las aristas representan la cercanía geográfica.
            
            **🔍 Hallazgos:**
            * Apliqué algoritmos de **Clustering** para detectar "zonas culturales" densas.
            * Usé **PageRank** para identificar los museos más "centrales" e influyentes de la red.
            """)
        
        with col_code:
            st.markdown("📄 **Snippet de mi Código (Construcción del Grafo):**")
            st.code('''
import networkx as nx

# Crear el grafo vacío
G = nx.Graph()

# Añadir nodos (Museos) y conexiones
for museo in lista_museos:
    G.add_node(museo['nombre'], pos=(museo['lat'], museo['lon']))
    
# Calcular métricas de centralidad
centralidad = nx.betweenness_centrality(G)

# Encontrar el museo "puente" más importante
top_museo = max(centralidad, key=centralidad.get)
print(f"Museo central: {top_museo}")
            ''', language='python')

    # --- PROYECTO 3: DATOS NACIONALES ---
    with tab3:
        st.header("Correlaciones en Datos Públicos de Argentina")
        st.caption("🛠️ Stack: SQL (DuckDB) | Seaborn | Pandas")
        
        col_text, col_code = st.columns([1, 1.3])

        with col_text:
            # 1. IMAGEN
            try:
                st.image("Datos_Nacionales.jpeg", caption="Correlación Educación vs Población", use_container_width=True)
            except FileNotFoundError:
                st.info("📷 (Acá iría la imagen 'Datos_Nacionales.jpeg')")

            st.divider()

            # 2. EXPLICACIÓN
            st.markdown("""
            **📌 Descripción:**
            Análisis exploratorio integrando múltiples fuentes de datos nacionales (Censo, Educación, Cultura).
            
            **📊 Tareas Realizadas:**
            1. **ETL:** Limpieza y normalización de datasets heterogéneos.
            2. **SQL:** Consultas complejas con DuckDB para cruzar grandes volúmenes de datos.
            3. **Visualización:** Análisis de la relación entre densidad poblacional y oferta educativa.
            """)
        
        with col_code:
            st.markdown("📄 **Snippet de mi Código (SQL):**")
            st.code('''
-- Consulta SQL para cruzar provincias y escuelas
SELECT 
    p.provincia,
    COUNT(e.id_escuela) as total_escuelas,
    p.poblacion_total,
    (p.poblacion_total / COUNT(e.id_escuela)) as ratio
FROM poblacion_argentina p
JOIN escuelas e ON p.id_provincia = e.id_provincia
GROUP BY p.provincia
HAVING total_escuelas > 100
ORDER BY total_escuelas DESC;
            ''', language='sql')
 
# --- SECCIÓN: HABILIDADES ---
elif seccion == "Habilidades":
    st.header("Stack Técnico y Herramientas 🛠️")
    st.write("---")

    # Usamos columnas para dividir Hard Skills (Técnicas) de Soft/Teóricas
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Lenguajes de Programación")
        
        # Python
        st.write("🐍 **Python (Data Science)**")
        st.progress(90) # Barra de progreso al 90%
        st.caption("Pandas | NumPy | Scikit-learn | Streamlit")
        
        # SQL
        st.write("🗄️ **SQL (Bases de Datos)**")
        st.progress(75)
        st.caption("DuckDB | Consultas Complejas | Joins")
        
        # Excel "Vitaminado"
        st.write("📊 **Excel Avanzado & Power Query**")
        st.progress(85)
        st.caption("ETL con Power Query | Tablas Dinámicas | Filtros | Funciones y Fórmulas")

    with col2:
        st.subheader("Fundamentos y Herramientas")
        
        # Teoría (Tu fuerte por la UBA)
        st.write("🧠 **Estadística y Probabilidad**")
        st.progress(90)
        st.caption("Variables Aleatorias | Distribuciones | Estadística Descriptiva")
        
        # Visualización
        st.write("📊 **Visualización de Datos**")
        st.progress(80)
        st.caption("Matplotlib | Seaborn | Power BI")
        
        # Idiomas (Ajustá el porcentaje según tu nivel real)
        st.write("🌎 **Inglés Técnico (Nivel B2)**")
        st.progress(70)
        st.caption("Lectura fluida de documentación técnica y papers científicos")

    st.write("---")
    
    # Un toque final: Habilidades Blandas (Soft Skills) con badges
    st.subheader("Habilidades Blandas")
    st.markdown("""
    <div style="display: flex; gap: 10px; flex-wrap: wrap;">
        <span style="background-color: #e0f7fa; color: #006064; padding: 5px 10px; border-radius: 15px; border: 1px solid #006064;">🧠 Pensamiento Crítico</span>
        <span style="background-color: #e0f7fa; color: #006064; padding: 5px 10px; border-radius: 15px; border: 1px solid #006064;">🗣️ Comunicación Efectiva</span>
        <span style="background-color: #e0f7fa; color: #006064; padding: 5px 10px; border-radius: 15px; border: 1px solid #006064;">🏃‍♂️ Disciplina y Resiliencia</span>
        <span style="background-color: #e0f7fa; color: #006064; padding: 5px 10px; border-radius: 15px; border: 1px solid #006064;">🤝 Trabajo en Equipo</span>
    </div>
    """, unsafe_allow_html=True)


# --- SECCIÓN: CONTACTO ---
elif seccion == "Contacto":
    st.header("📬 Conectemos")

    st.write("---")

    col_izq, col_der = st.columns([1.5, 1])

    with col_izq:
        st.subheader("¿Buscas un perfil analítico y proactivo?")
        st.markdown("""
        Estoy buscando activamente mi primera experiencia profesional fuerte como **Data Analyst** o **Data Scientist Junior**.
        
        **¿Qué puedo aportar a tu equipo?**
        * ✅ **Capacidad Técnica:** Python, SQL y manejo de datos complejos.
        * ✅ **Rigor Académico:** Formación sólida en la UBA (Promedio 9.50).
        * ✅ **Disciplina:** La constancia del deporte aplicada al trabajo.

        Si tenés un desafío en **Finanzas, Salud o Tecnología**, me encantaría escuchar sobre él.
        """)
        
        # Espacio
        st.write("") 
        
        # Botón para descargar CV (Reemplazá 'CV_Francisco.pdf' con tu archivo real)
        # Es clave tenerlo acá también al final de la página.
        # try:
        #     with open("CV_Francisco_Peix.pdf", "rb") as pdf_file:
        #         st.download_button(
        #             label="📄 Descargar mi CV Completo",
        #             data=pdf_file,
        #             file_name="CV_Francisco_Peix.pdf",
        #             mime="application/pdf",
        #         )
        # except FileNotFoundError:
        #     st.warning("⚠️ (El archivo del CV no está en la carpeta)")

        st.link_button("📄 Ver mi CV Completo", "https://drive.google.com/file/d/1qiMh6Zk--kHo3uoHwp9MQjBfBiGXmz8I/view?usp=sharing")

    with col_der:
        # Hacemos un "Card" visual para los datos de contacto
        st.info("💡 **Mis Canales**")
        
        # Usamos link_button para que parezcan botones reales
        st.link_button("📧 Enviar Email", "mailto:franpeix01@gmail.com", use_container_width=True)
        st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/francisco-peix-1884092a8", use_container_width=True)
        st.link_button("🐙 GitHub", "https://github.com/franpeix", use_container_width=True)
    
    st.write("---")
    
    # Pie de página centrado
    st.markdown("<div style='text-align: center'>Desarrollado con ❤️ y 🐍 Python por Francisco</div>", unsafe_allow_html=True)
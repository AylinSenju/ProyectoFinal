<div align="center">
<h1><b><u>Proyecto Final</u></b></h1>
</div>
<div>
  <h3> <b>Integrantes:</b> </h3>
  <div>
    <ul>
      <li>Gonzalez Preciado Angel Javier</li>
      <li>Gonzalez Ramirez Biron Jahdiel</li>
      <li>Mascareño Zendejas Aylin Yael</li>
      <li>Ramirez Velazquez Sherlyn</li>
      <li>Tapia Carro Angelica Vanesa</li>
    </ul>
  </div>
</div> 
<hr>
<div>
  <h3> <b>Proposito del Proyecto</b> </h3>
  <p>El objetivo de este proyecto es recopilar información clave sobre películas y series de televisión mediante técnicas de navegación web, con especial énfasis en datos como nombre, valoración, género y director.
El objetivo es organizar y almacenar esta información en una base de datos estructurada que facilite el análisis, permitiéndote identificar tendencias, descubrir géneros populares o analizar tu trabajo. Luego se creará un panel interactivo que proporcionará información transparente y accesible sobre los datos recopilados, mejorando la toma de decisiones en proyectos cinematográficos y de entretenimiento.</p>
</div>
<hr>
<div>
  <h3> <b>Etapas</b> </h3>
  <p>El proyecto constará en tres etapas clave, basadas en el proceso de ETL (Extracción, Transformación, Carga) , que se describe a continuación:</p>
  <ol>
    <li><b>Extracción:</b></li> 
    <p>En esta etapa, se realizará el proceso de web scraping para recopilar información clave de películas y series</p>
    <li><b>Transformación:</b></li>
    <p>Los datos extraídos serán procesados ​​para garantizar su calidad y consistencia, incluyendo:</p>
      <ul>
        <li>Limpieza de datos (eliminación de duplicados y datos incompletos).</li>
        <li>Normalización (formato uniforme en nombres y fechas).</li> 
        <li>Estructuración (organización en un formato adecuado para la base de datos).</li>
      </ul>
    <p></p>
    <li><b>Carga:</b></li>
    <p>Finalmente, los datos transformados serán migrados a una base de datos relacional, donde podrán ser consultados de manera eficiente. Además, se diseñará un tablero interactivo para visualizar y analizar la información recopilada, proporcionando información útil para futuros análisis. </p>
  </ol>
</div>
<hr>
<div>
  <h3><b>Resultados Esperados</b></h3>
  <p>Los usuarios podrán acceder a una plataforma que les permitirá extraer, organizar y mostrar de manera eficiente datos clave de películas y series. El sistema debe poder recopilar información precisa a través del web scraping, almacenar esa información en una base de datos con precisión y proporcionar a los usuarios un panel interactivo para explorar estos datos, lo que facilita la identificación de patrones, tendencias y la toma de decisiones en la industria del entretenimiento.
</p>
</div>
<hr>
<div>
   <h3>Instrucciones</h3>
   <p>
   NOTA 1: Puede directamente correr el archivo "pagina", esto debido a que ya se tiene cargada la informacion y directamente revisar los dashboards de la pagina. para no perder tiempo ;)
   </p>
   <p>1.- Seleccione el archivos Web_scraping, este realizara una busqueda por la pagina de sensacine.com, obtieniendo informacion acerca de peliculas y series
   , y despues de eso se guardara en un archivo CSV.
   </p>
   <p>
     2.- Seleccione el archivo de limpieza, que limpiara en caso de que se necesite, asi como cambiara el formato del de las fechas y las calificaciones para que lo pueda leer correctamente MySQL y deespues 
      guardaran un archivos CSV que este limpio para despues guardarlo en MySQL.
   </p>
   <p>
     3.- Despues de eso seleccione los archivos de Migracion_series y Migracion_peliculas, los cuales se encargaran de pasar los datos del CSV a una base de datos con dos tablas, una sera dedicada a series y otra      a peliculas con sus respectivas columnas y registros.
   </p>
   <p>
     4.- Seleccione el archivo pagina, donde despues de correrlo se vera una direccion donde se accede y se muestran toda la informacion, asi como los dashboards
   </p>
  <p>
    NOTA 2: Los archivos peliculas y series son las estructuras de los dashboard, y el archivo informacion, es para dar un poco de contexto de la realizacion del proyecto, asi como los nombres de los integrantes
  </p>
</div>
</hr>
<hr>
<div>
<h3>Librerias utilizadas</h3>
<p>dash: Se utiliza en este proyecto para la creacion visual de los dashboard.

<p>dash_bootstrap_components: Nos brinda componentes pre-diseñados y responsivos que mejoran la apariencia de las aplicaciones Dash.</p>
<p>pandas: Se uriliza para la limpieza de datos, asi como para pasar de Dataframe a CSV y para leer MySQL.</p>
<p>mysql.connector: Se utiliza para lamigracion de peliculas y series hacia MySQL.</p>
<p>plotly: Nos ayuda a crear graficos intractivos.</p>
<p>webdriver_manager: Para poder movernos a traves de las paginas web al hacer nuestro Bot que recolecta infromacion paara despues analizarla</p>
<p>Selenium: Nos ayuda a automatizar  navegadores web para tareas como pruebas o scraping.</p>
<p>bs4: Se utiliza para analizar documentos HTML que obtenemos, esto para su posterior guardado.</p>
</div>
</hr>




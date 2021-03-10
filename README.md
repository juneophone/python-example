# Python Example
Study the example of python.

## Detect AI:

<details>
  
  <summary>Detect Object</summary>  
  
  * Docker File : [Download](./dockerfiles/Dockerfile.Detect_object)
  * Training module yolo.h5 : [Download](https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5)
  
  * File Name : [detect_object.py](./detect_ai/detect_object.py) 
  * Result
  
  <table width="100%" align="center" border="0">    
    <tr>
      <td width="50%" align="center">befor</td>
      <td width="50%" align="center">after</td>
    </tr>
    <tr>
      <td width="50%" align="center"><img src="./demo_image/brid_03.jpg" width="300"></td>
      <td width="50%" align="center"><img src="./reader.images/example_result_01.jpg" width="300"></td>
    </tr>    
  </table>
  
</details>

<details>
  
  <summary>Detect Color</summary>  
  
  * Docker File : [Download](./dockerfiles/Dockerfile.Detect_object)  
  
  * File Name : [detect_color_01.py](./detect_ai/detect_color_01.py) 
  * Result
  
  <table width="100%" align="center" border="0">    
    <tr>
      <td width="30%" align="center">Original</td>
      <td width="30%" align="center">Mask</td>
      <td width="30%" align="center">Result</td>
    </tr>
    <tr>
      <td width="30%" align="center"><img src="./demo_image/brid_02.jpg" width="300"></td>
      <td width="30%" align="center"><img src="./reader.images/detect_color_01_brid_02_mask.png" width="300"></td>
      <td width="30%" align="center"><img src="./reader.images/detect_color_01_brid_02_result.png" width="300"></td>
    </tr>    
  </table>
  
  * File Name : [detect_color_02.py](./detect_ai/detect_color_02.py) 
  * Result
  
  <table width="100%" align="center" border="0">    
    <tr>
      <td width="30%" align="center">Original</td>
      <td width="30%" align="center">Mask</td>
      <td width="30%" align="center">Result</td>
    </tr>
    <tr>
      <td width="30%" align="center"><img src="./demo_image/brid_03.jpg" width="300"></td>
      <td width="30%" align="center"><img src="./reader.images/detect_color_02_brid_03_mask.png" width="300"></td>
      <td width="30%" align="center"><img src="./reader.images/detect_color_02_brid_03_result.png" width="300"></td>
    </tr>    
  </table>
  
</details>

## Image Process

<details>
  
  <summary>Sketches (素描圖)</summary>
  
  * File Name : [sketches.py](./image_process/sketches.py)
  * Result
  
  <table width="100%" align="center" border="0">    
    <tr>
      <td width="30%" align="center">Original</td>
      <td width="30%" align="center">Color</td>
      <td width="30%" align="center">Gray</td>      
    </tr>
    <tr>
      <td width="30%" align="center"><img src="./demo_image/brid_01.jpg" width="300"></td>
      <td width="30%" align="center"><img src="./reader.images/sketches_01.png" width="300"></td>
      <td width="30%" align="center"><img src="./reader.images/sketches_02.png" width="300"></td>      
    </tr>
    <tr>
      <td width="30%" align="center">Original</td>
      <td width="30%" align="center">Color</td>
      <td width="30%" align="center">Gray</td>
    </tr>
    <tr>
      <td width="30%" align="center"><img src="./demo_image/brid_02.jpg" width="300"></td>
      <td width="30%" align="center"><img src="./reader.images/sketches_03.png" width="300"></td>
      <td width="30%" align="center"><img src="./reader.images/sketches_04.png" width="300"></td>
    </tr>
  </table>
  
</details>

<details>
  
  <summary>S-Curve</summary>
  
  * File Name : [s-curve_01.py](./image_process/s-curve_01.py)
  * Result
  
  <table width="100%" align="center" border="0">    
    <tr>
      <td width="30%" align="center">k = 0.1</td>
      <td width="30%" align="center">k = 0.05</td>         
    </tr>
    <tr>      
      <td width="50%" align="center"><img src="./reader.images/s-curve_0.1.png" width="500"></td>
      <td width="50%" align="center"><img src="./reader.images/s-curve_0.05.png" width="500"></td>      
    </tr>    
  </table>
  
</details>

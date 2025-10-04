# 📄 Bayesian symbolic regression: Automated equation discovery from physicists' perspective
**Autores: Roger Guimera & Marta Sales-Pardo**  
**Año / Conferencia / Journal: 2025 / The Royal Society**  
**Enlace / DOI: https://doi.org/10.48550/arXiv.2507.19540**  

---

## 🧩 Contexto
- Regresión simbólica
- Se comparan dos enfoques distintos: heurística y probabilística

---

## 🎯 Objetivos del paper
- Aportar una nueva perspectiva en el desarrollo de la regresión simbólica

---

## 🏗️ Metodología / Modelo propuesto
- Se crea un algoritmo con elementos de probabilidad bayesiana para encontrar el modelo que mejor ajusta los datos
- A diferencia del método tradicional no requiere tener en cuenta la pérdida, bondad de ajuste y la complejidad, ya que, esto está considerado por la teoría de probabilidad al maximizar la posteriori

---

## 📊 Experimentos
- Se comparan ambos métodos en dos ejemplos simples, una función lineal y una función constante. En ambos casos, se consideran distinta cantidad de datos totales y se les agrega ruido a través de un error gaussiano de media 0 y con distitntos valores de varianza. Ambos métodos funcionan bien cuando el ruido es bajo, sin embargo, al aumentar el ruido el método tradicional tiende a sobreajustar los valores


---

## ⚖️ Limitaciones
- Los experimentos se realizan con una librería ya implementada (https://bitbucket.org/rguimera/machine-scientist/src/no_degeneracy/) no se discute la construcción del modelo

---

## 💡 Ideas útiles para mi trabajo
- Puede ser interesante considerar el enfoque probabilístico



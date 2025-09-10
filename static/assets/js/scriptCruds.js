  // agregar fila a cualquier tabla
  function agregarFila(formId, tablaId, nombreInput, columnaNombre) {
    const form = document.getElementById(formId);
    const tabla = document.getElementById(tablaId);

    form.addEventListener('submit', function(e){
      e.preventDefault();
      const nombre = this[nombreInput].value.trim();
      if(nombre){
        // si está el mensaje "No hay registros" se quita
        if(tabla.querySelector('td[colspan="2"]')){
          tabla.innerHTML = '';
        }

        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td>${nombre}</td>
          <td class="text-end">
            <button class="btn btn-sm btn-outline-secondary me-2">Editar</button>
            <button class="btn btn-sm btn-outline-danger">Eliminar</button>
          </td>
        `;
        tabla.appendChild(tr);
        this.reset();
      }
    });
  }

  // se inicializan los cruds
  agregarFila('formPropiedades', 'tablaPropiedades', 'nombre_propiedad', 'Propiedad');
  agregarFila('formDisponibilidad', 'tablaDisponibilidad', 'nombre_disponibilidad', 'Disponibilidad');
  agregarFila('formVentaArriendo', 'tablaVentaArriendo', 'nombre_venta', 'Venta/Arriendo');
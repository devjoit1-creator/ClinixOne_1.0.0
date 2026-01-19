let tableEmpresa = new DataTable('#tablaEmpresa', {
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})

let tableUsuarios = new DataTable('#tablaUsuarios', {
  language: {
    lengthMenu: "Mostrar _MENU_ registros por pagina",
    zeroRecords: "Sin registros encontrados",
    info: "Mostrando pagina _PAGE_ de _PAGES_",
    infoEmpty: "No hay registros disponibles",
    infoFiltered: "(filtrado de _MAX_ registros)",
    search: "Filtrar:",
    paginate: {
      first: "Primera",
      last: "Última",
      next: "Siguiente",
      previous: "Anterior"
    },
    columnDefs: [
      { width: 10, targets: 0 },
      { width: 100, targets: 1 }
    ]
  }
});

let tablePacientes = new DataTable('#tablaPacientes', {
    language: {
        lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
            first: "Primera",
            last: "Última",
            next: "Siguiente",
            previous: "Anterior"
          },
        columnDefs: [
          { width: 10, targets: 0 },
          { width: 100, targets: 1 }
        ]  
    }
});

let tableCargosAsistenciales = new DataTable('#tablaCargosAsistenciales',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        },
        columnDefs: [
          { width: 10, targets: 0 },
          { width: 90, targets: 1 }
        ] 
  }
})

let tableMedicos = new DataTable('#tablaMedicos',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        },
        columnDefs: [
          { width: 10, targets: 0 },
          { width: 90, targets: 1 }
        ] 
  }
})

let tableDatosMedico = new DataTable('#tablaDatosMedico',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        },
        columnDefs: [
          { width: 10, targets: 0 },
          { width: 90, targets: 1 }
        ] 
  }
})

let tableUnidadesFuncionales = new DataTable('#tablaUnidadesFuncionales',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        },
        columnDefs: [
          { width: 10, targets: 0 },
          { width: 90, targets: 1 }
        ] 
  }
})

let tableHabitaciones = new DataTable('#tablaHabitaciones',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})

let tableTarifas = new DataTable('#tablaTarifas',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})

let tableGruposServicios = new DataTable('#tablaGruposServicios',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})

let tableServicios = new DataTable('#tablaServicios',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})

let tableBusquedaGrupos = new DataTable('#tablaBusquedaGrupos',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})

let tableAdministradoras = new DataTable('#tablaAdministradoras',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})

let tableBusquedaPacientesPrev = new DataTable('#tablaBusquedaPacientesPrev',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})

let tableBusquedaDiagnosticosPrev = new DataTable('#tablaBusquedaDiagnosticosPrev',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})

let tablePrevaloraciones = new DataTable('#tablaPrevaloraciones',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})

let tableBusquedaPacientesConsultas = new DataTable('#tablaBusquedaPacientesConsultas',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})

let tableBusquedaAdminsConsultas = new DataTable('#tablaBusquedaAdminsConsultas',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})

let tableBusquedaDiagnosticosConsultas = new DataTable('#tablaBusquedaDiagnosticosConsultas',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})

let tableBusquedaServicioAsoConsultas = new DataTable('#tablaBusquedaServicioAsoConsultas',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})


let tableBusquedaServiciosConsultas = new DataTable('#tablaBusquedaServiciosConsultas',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})
/* Cambios en Panel de Consultas */
/* let tableConsultas = new DataTable('#tablaConsultas',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
}) */

/* Cambios en Panel de Atenciones Consulta */
/* let tableAtenciones = new DataTable('#tablaAtenciones',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
}) */

/* Cambios en Panel de Atenciones Consulta */
/* let tableAtencionesHosp = new DataTable('#tablaAtencionesHosp',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
}) */

/* Datatables de Hospitalización */
/* let tableHospitalizacion = new DataTable('#tablaHospitalizacion',{
  initComplete: function () {
        this.api()
            .columns()
            .every(function () {
                let column = this;
                let title = column.footer().textContent;
 
                // Create input element
                let input = document.createElement('input');
                input.placeholder = title;
                column.footer().replaceChildren(input);
 
                // Event listener for user input
                input.addEventListener('keyup', () => {
                    if (column.search() !== this.value) {
                        column.search(input.value).draw();
                    }
                });
            });
    },
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
}) */

let tableBusquedaPacientesHospitalizacion = new DataTable('#tablaBusquedaPacientesHospitalizacion',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})

let tableBusquedaAdminsHospitalizacion = new DataTable('#tablaBusquedaAdminsHospitalizacion',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})

let tableBusquedaPacientesAnexos = new DataTable('#tablaBusquedaPacientesAnexos',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})

let tableBusquedaPacientesEpicrisis = new DataTable('#tablaBusquedaPacientesEpicrisis',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})

/* Cambios en Panel de Busqueda de Habitaciones */
/* let tableHabitacionesModal = new DataTable('#tablaHabitacionesModal',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
}) */

let tablaBusquedaDiagnosticosHospitalizacion = new DataTable('#tablaBusquedaDiagnosticosHospitalizacion',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
    zeroRecords: "Sin registros encontrados",
    info: "Mostrando pagina _PAGE_ de _PAGES_",
    infoEmpty: "No hay registros disponibles",
    infoFiltered: "(filtrado de _MAX_ registros)",
    search: "Filtrar",
    paginate: {
      first: "Primera",
      last: "Última",
      next: "Siguiente",
      previous: "Anterior"
    }
  }
})

let tableBusquedaDiagnosticosEgresoHosp = new DataTable('#tablaBusquedaDiagnosticosEgresoHosp',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
    zeroRecords: "Sin registros encontrados",
    info: "Mostrando pagina _PAGE_ de _PAGES_",
    infoEmpty: "No hay registros disponibles",
    infoFiltered: "(filtrado de _MAX_ registros)",
    search: "Filtrar",
    paginate: {
      first: "Primera",
      last: "Última",
      next: "Siguiente",
      previous: "Anterior"
    }
  }
})

let tableBusquedaServiciosHosp = new DataTable('#tablaBusquedaServiciosHosp',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
    zeroRecords: "Sin registros encontrados",
    info: "Mostrando pagina _PAGE_ de _PAGES_",
    infoEmpty: "No hay registros disponibles",
    infoFiltered: "(filtrado de _MAX_ registros)",
    search: "Filtrar",
    paginate: {
      first: "Primera",
      last: "Última",
      next: "Siguiente",
      previous: "Anterior"
    }
  }
})

let tableRecomendaciones = new DataTable('#tablaRecomendaciones',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  },
  order: [[0, 'desc']]
})

let tableIncapacidades = new DataTable('#tablaIncapacidades',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  },
  order: [[0, 'desc']]
})

let tableBusquedaDiagnosticosIncap = new DataTable('#tablaBusquedaDiagnosticosIncap',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})

let tableInterconsultas = new DataTable('#tablaInterconsultas',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  },
  order: [[0, 'desc']]
})

let tableOrdenesDiagnosticas = new DataTable('#tablaOrdenesDiagnosticas',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  },
  order: [[0, 'desc']]
})

let tableBusquedaProcedimientosCups = new DataTable('#tablaBusquedaProcedimientosCups',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})

let tableBusquedaEspecialidadesInter = new DataTable('#tablaBusquedaEspecialidadesInter',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})

let tableNutricion = new DataTable('#tablaNutricion',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  },
  order: [[0, 'desc']]
})

let tableBusquedaDiagnosticosNutricion = new DataTable('#tablaBusquedaDiagnosticosNutricion',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})

let tablePsicologia = new DataTable('#tablaPsicologia',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  },
  order: [[0, 'desc']]
});

let tableBusquedaDiagnosticosPsicologia = new DataTable('#tablaBusquedaDiagnosticosPsicologia',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})

let tableTerceros = new DataTable('#tablaTerceros',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})

let tableCuentas = new DataTable('#tablaCuentas',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})

let tableFuentes = new DataTable('#tablaFuentes',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})

let tableFacturas = new DataTable('#tablaFacturas',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})


let tableBusquedaTercerosFacturas = new DataTable('#tablaBusquedaTercerosFacturas',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})

let tableBusquedaServiciosTerceros = new DataTable('#tablaBusquedaServiciosTerceros',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})

let tableResFacturacion = new DataTable('#tablaResFacturacion',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})

let tableNotasCredito = new DataTable('#tablaNotasCredito',{
  language:{
    lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Sin registros encontrados",
        info: "Mostrando pagina _PAGE_ de _PAGES_",
        infoEmpty: "No hay registros disponibles",
        infoFiltered: "(filtrado de _MAX_ registros)",
        search: "Filtrar:",
        paginate: {
          first: "Primera",
          last: "Última",
          next: "Siguiente",
          previous: "Anterior"
        }
  }
})
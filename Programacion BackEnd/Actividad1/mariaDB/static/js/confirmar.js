function confirmarEliminacion(id){
    Swal.fire({
        title: '¿Está Seguro?',
        text: "No Podrás Deshacer Está Acción!🤨",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, eliminar!',
        cancelButtonText: 'Cancelar'
      }).then((result) => {
        if (result.isConfirmed) {
          window.location.href = "/eliminar_reserva/"+id+"/";
        }
      })
}
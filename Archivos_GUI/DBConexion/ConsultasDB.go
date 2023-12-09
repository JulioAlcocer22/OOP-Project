package DBConexion

import (
	"Model"
	"database/sql"
	"log"
)

func ObtenerLicenciaturas(universidad string) (opcionesLicenciatura []Model.Licenciatura) {
	db, err := ObtenerConexion()
	defer db.Close()
	if err != nil {
		log.Fatal("Error realizando la conexion a la base de datos", err.Error())
	}

	rows, err := db.Query("SELECT * FROM dbo.RecuperarCarreras(@universidad)", sql.Named("universidad", universidad))
	defer rows.Close()
	if err != nil {
		log.Fatal("Error al realizar la consulta asociada a las licenciaturas", err.Error())
	}

	for rows.Next() {
		var licenciatura Model.Licenciatura
		err := rows.Scan(&licenciatura.LicenciaturaItem)
		if err != nil {
			log.Fatal("Error al obtener los datos de las licenciaturas", err.Error())
		}
		opcionesLicenciatura = append(opcionesLicenciatura, licenciatura)
	}
	return
}

func ObtenerUniversidades() (opcionesUniversidad []Model.Universidad) {
	db, err := ObtenerConexion()
	defer db.Close()
	if err != nil {
		log.Fatal("Error realizando la conexion a la base de datos", err.Error())
	}

	rows, err := db.Query("SELECT * FROM dbo.RecuperarUniversidades()")
	defer rows.Close()
	if err != nil {
		log.Fatal("Error realizando consulta para recuperar universidades", err.Error())
	}

	for rows.Next() {
		var universidad Model.Universidad
		err := rows.Scan(&universidad.UniversidadItem)
		if err != nil {
			log.Fatal("Error al obtener las universidades", err.Error())
		}
		opcionesUniversidad = append(opcionesUniversidad, universidad)
	}
	return
}

func obtenerEmpresas(universidad string, licenciatura string) (resultadosEmpresas []Model.Empresa) {
	db, err := ObtenerConexion()
	defer db.Close()
	if err != nil {
		log.Fatal("Error realizando la conexion a la base de datos", err.Error())
	}

	rows, err := db.Query("EXECUTE dbo.AnalisisEmpresas @universidad, @licenciatura", sql.Named("universidad", universidad), sql.Named("licenciatura", licenciatura))
	defer rows.Close()
	if err != nil {
		log.Fatal("Error realizando la consulta a la base de datos", err.Error())
	}

	for rows.Next() {
		var empresa Model.Empresa
		err := rows.Scan(&empresa.EmpresaItem, &empresa.PorcentajeItem)
		if err != nil {
			log.Fatal("Error ejecutando la consulta de las empresas", err.Error())
		}

		resultadosEmpresas = append(resultadosEmpresas, empresa)
	}
	return
}

func obtenerRoles(universidad string, licenciatura string) (resultadosRoles []Model.Rol) {
	db, err := ObtenerConexion()
	defer db.Close()
	if err != nil {
		log.Fatal("Error realizando la conexión a la base de datos", err.Error())
	}

	rows, err := db.Query("EXECUTE dbo.AnalisisRoles @universidad, @licenciatura", sql.Named("universidad", universidad), sql.Named("licenciatura", licenciatura))
	defer rows.Close()
	if err != nil {
		log.Fatal("Error al ejecutar la consulta asociada a los roles", err.Error())
	}

	for rows.Next() {
		var rol Model.Rol
		err := rows.Scan(&rol.RolItem, &rol.PorcentajeItem)
		if err != nil {
			log.Fatal("Error al obtener los datos de los roles", err.Error())
		}
		resultadosRoles = append(resultadosRoles, rol)
	}
	return
}

func obtenerDuracion(universidad string, licenciatura string) (resultadosDuracion []Model.Duracion) {
	db, err := ObtenerConexion()
	defer db.Close()
	if err != nil {
		log.Fatal("Error realizando la conexión a la base de datos", err.Error())
	}

	rows, err := db.Query("EXECUTE dbo.PromedioDuracion @universidad, @licenciatura", sql.Named("universidad", universidad), sql.Named("licenciatura", licenciatura))
	defer rows.Close()
	if err != nil {
		log.Fatal("Error al ejecutar la consulta asociada a la duracion", err.Error())
	}

	for rows.Next() {
		var duracion Model.Duracion
		err := rows.Scan(&duracion.DuracionItem)
		if err != nil {
			log.Fatal("Error al obtener los datos de duracion", err.Error())
		}
		resultadosDuracion = append(resultadosDuracion, duracion)
		//fmt.Println(duracion.DuracionItem)
	}
	return
}

func ObtenerResultados(universidad string, licenciatura string) (resultadosFinales Model.DatosFinales) {
	resultadosFinales.Empresa = obtenerEmpresas(universidad, licenciatura)
	resultadosFinales.Rol = obtenerRoles(universidad, licenciatura)
	resultadosFinales.Duracion = obtenerDuracion(universidad, licenciatura)
	return
}

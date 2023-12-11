package Model

type DatosEntrada struct {
	UniversidadItem  string `json:"UniversidadItem"`
	LicenciaturaItem string `json:"LicenciaturaItem"`
}

type Licenciatura struct {
	LicenciaturaItem string `json:"Degree"`
}

type Universidad struct {
	UniversidadItem string `json:"University"`
}

type Empresa struct {
	EmpresaItem    string  `json:"EmpresaItem"`
	PorcentajeItem float64 `json:"PorcentajeItem"`
}

type Rol struct {
	RolItem        string  `json:"RolItem"`
	PorcentajeItem float64 `json:"PorcentajeItem"`
}

type Duracion struct {
	DuracionItem float64 `json:"DuracionItem"`
}

type DatosFinales struct {
	Empresa  []Empresa  `json:"Empresa"`
	Rol      []Rol      `json:"Rol"`
	Duracion []Duracion `json:"Duracion"`
}

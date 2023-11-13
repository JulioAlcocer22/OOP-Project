/****** Object:  Table [dbo].[Experiencia]    Script Date: 12/11/2023 05:36:02 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Experiencia](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[IdEgresado] [int] NULL,
	[Empresa] [varchar](255) NULL,
	[Puesto] [varchar](255) NULL,
	[Descripcion] [varchar](255) NULL,
	[Duracion] [int] NULL,
	[FechaInicio] [date] NULL,
	[FechaFin] [date] NULL,
PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
UNIQUE NONCLUSTERED 
(
	[IdEgresado] ASC,
	[Empresa] ASC,
	[Puesto] ASC,
	[Descripcion] ASC,
	[Duracion] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Experiencia]  WITH CHECK ADD FOREIGN KEY([IdEgresado])
REFERENCES [dbo].[EgresadoInfo] ([Id])
GO

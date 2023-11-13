/****** Object:  Table [dbo].[EgresadoInfo]    Script Date: 12/11/2023 05:36:02 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[EgresadoInfo](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[IdLink] [int] NULL,
	[Nombre] [varchar](255) NULL,
	[Universidad] [varchar](255) NULL,
	[Carrera] [varchar](255) NULL,
PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
UNIQUE NONCLUSTERED 
(
	[IdLink] ASC,
	[Nombre] ASC,
	[Universidad] ASC,
	[Carrera] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[EgresadoInfo]  WITH CHECK ADD FOREIGN KEY([IdLink])
REFERENCES [dbo].[LinkEgresados] ([Id])
GO

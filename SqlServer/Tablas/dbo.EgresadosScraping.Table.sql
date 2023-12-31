/****** Object:  Table [dbo].[EgresadosScraping]    Script Date: 02/10/2023 11:47:36 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[EgresadosScraping](
	[Link] [varchar](100) NULL,
	[Nombre] [varchar](50) NOT NULL,
	[Empresa] [varchar](50) NOT NULL,
	[Universidad] [varchar](50) NULL,
	[Carrera] [varchar](50) NULL,
	[Descripcion] [varchar](200) NULL,
	[Duracion] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[Nombre] ASC,
	[Empresa] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[EgresadosScraping]  WITH CHECK ADD  CONSTRAINT [fk_LinkEgresados] FOREIGN KEY([Link])
REFERENCES [dbo].[LinkEgresados] ([Link])
GO
ALTER TABLE [dbo].[EgresadosScraping] CHECK CONSTRAINT [fk_LinkEgresados]
GO

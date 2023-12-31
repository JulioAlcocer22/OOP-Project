/****** Object:  Table [dbo].[Egresados]    Script Date: 02/10/2023 11:47:36 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Egresados](
	[Nombre] [varchar](50) NOT NULL,
	[Empresa] [varchar](50) NOT NULL,
	[Rol] [varchar](200) NULL,
PRIMARY KEY CLUSTERED 
(
	[Nombre] ASC,
	[Empresa] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Egresados]  WITH CHECK ADD  CONSTRAINT [fk_EgresadosScraping] FOREIGN KEY([Nombre], [Empresa])
REFERENCES [dbo].[EgresadosScraping] ([Nombre], [Empresa])
GO
ALTER TABLE [dbo].[Egresados] CHECK CONSTRAINT [fk_EgresadosScraping]
GO

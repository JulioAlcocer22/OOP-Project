/****** Object:  Table [dbo].[Egresados]    Script Date: 12/11/2023 05:36:02 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Egresados](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[IdEgresado] [int] NULL,
	[IdExperiencia] [int] NULL,
	[Rol] [varchar](255) NULL,
PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
UNIQUE NONCLUSTERED 
(
	[IdEgresado] ASC,
	[IdExperiencia] ASC,
	[Rol] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Egresados]  WITH CHECK ADD FOREIGN KEY([IdEgresado])
REFERENCES [dbo].[EgresadoInfo] ([Id])
GO
ALTER TABLE [dbo].[Egresados]  WITH CHECK ADD FOREIGN KEY([IdExperiencia])
REFERENCES [dbo].[Experiencia] ([Id])
GO

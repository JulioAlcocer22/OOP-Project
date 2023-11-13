/****** Object:  StoredProcedure [dbo].[Roles]    Script Date: 12/11/2023 05:36:02 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:      <Author, , Name>
-- Create Date: <Create Date, , >
-- Description: <Description, , >
-- =============================================
CREATE PROCEDURE [dbo].[Roles]
(
    @Universidad VARCHAR(255),
	@Carrera VARCHAR(255)
)
AS
BEGIN
    SET NOCOUNT ON

	DECLARE @TotalRol INT

	SET @TotalRol = (SELECT COUNT(Rol) FROM Egresados)

    SELECT Egresados.Rol, 100.0*COUNT(EgresadoInfo.Nombre)/@TotalRol AS 'Porcentaje'
	FROM Egresados JOIN EgresadoInfo ON Egresados.IdEgresado = EgresadoInfo.Id 
	JOIN Experiencia ON Egresados.IdExperiencia = Experiencia.Id
	WHERE EgresadoInfo.Universidad = @Universidad
	AND EgresadoInfo.Carrera = @Carrera
	GROUP BY Egresados.Rol
END
GO

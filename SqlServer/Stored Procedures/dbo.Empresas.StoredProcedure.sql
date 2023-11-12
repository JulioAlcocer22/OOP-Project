/****** Object:  StoredProcedure [dbo].[Empresas]    Script Date: 12/11/2023 05:36:02 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:      <Author, , Name>
-- Create Date: <Create Date, , >
-- Description: <Description, , >
-- =============================================
CREATE PROCEDURE [dbo].[Empresas]
(
    @Universidad VARCHAR(255),
	@Carrera VARCHAR(255)
)
AS
BEGIN
    SET NOCOUNT ON

	DECLARE @EgresadosUnicos INT

	SET @EgresadosUnicos = (SELECT COUNT(DISTINCT Nombre) FROM EgresadoInfo)

    SELECT Experiencia.Empresa, 100.0*COUNT(DISTINCT EgresadoInfo.Nombre)/@EgresadosUnicos AS 'Porcentaje'
	FROM Egresados JOIN EgresadoInfo ON Egresados.IdEgresado = EgresadoInfo.Id 
	JOIN Experiencia ON Egresados.IdExperiencia = Experiencia.Id
	WHERE EgresadoInfo.Universidad = @Universidad
	AND EgresadoInfo.Carrera = @Carrera
	GROUP BY Experiencia.Empresa
END
GO

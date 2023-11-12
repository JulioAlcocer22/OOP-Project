/****** Object:  StoredProcedure [dbo].[PromedioDuracion]    Script Date: 12/11/2023 05:36:02 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:      <Author, , Name>
-- Create Date: <Create Date, , >
-- Description: <Description, , >
-- =============================================
CREATE PROCEDURE [dbo].[PromedioDuracion]
(
    @Universidad VARCHAR(255),
	@Carrera VARCHAR(255)
)
AS
BEGIN
    SET NOCOUNT ON

    SELECT CAST(SUM(Experiencia.Duracion) AS FLOAT)/COUNT(Experiencia.Duracion)
	FROM Egresados JOIN EgresadoInfo ON Egresados.IdEgresado = EgresadoInfo.Id 
	JOIN Experiencia ON Egresados.IdExperiencia = Experiencia.Id
	WHERE EgresadoInfo.Universidad = @Universidad
	AND EgresadoInfo.Carrera = @Carrera
END
GO

/****** Object:  StoredProcedure [dbo].[PromedioDuracion]    Script Date: 02/10/2023 11:47:36 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[PromedioDuracion] ( @Universidad varchar(50) )
AS
BEGIN
    SET NOCOUNT ON

	IF OBJECT_ID('tempdb.dbo.#Egresados', 'U') IS NOT NULL
		DROP TABLE #Egresados; 

	SELECT *
	INTO #Egresados
	FROM EgresadosScraping
	WHERE Universidad = @Universidad

    SELECT AVG(Duracion) as 'Promedio' FROM #Egresados
END
GO

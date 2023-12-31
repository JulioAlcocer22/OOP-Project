/****** Object:  StoredProcedure [dbo].[AnalisisEmpresas]    Script Date: 02/10/2023 11:47:36 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[AnalisisEmpresas] ( @Universidad varchar(50) )
AS
BEGIN
    SET NOCOUNT ON

	IF OBJECT_ID('tempdb.dbo.#Egresados', 'U') IS NOT NULL
		DROP TABLE #Egresados; 

	DECLARE @TotalMuestra INT

	SELECT *
	INTO #Egresados
	FROM EgresadosScraping 
	WHERE Universidad = @Universidad

	SET @TotalMuestra = (SELECT COUNT(DISTINCT Nombre) FROM #Egresados)

    SELECT Empresa, COUNT(*)*100/@TotalMuestra AS 'Porcentaje' FROM #Egresados
	GROUP BY Empresa
END
GO

/****** Object:  StoredProcedure [dbo].[AnalisisRoles]    Script Date: 02/10/2023 11:47:36 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[AnalisisRoles] ( @Universidad varchar(50) )
AS
BEGIN
    SET NOCOUNT ON

	IF OBJECT_ID('tempdb.dbo.#Egresados', 'U') IS NOT NULL
		DROP TABLE #Egresados; 

	DECLARE @TotalMuestra INT

	SELECT *
	INTO #Egresados
	FROM EgresadosScraping a LEFT JOIN Egresados b	
	ON a.Nombre = b.Nombre AND a.Empresa = b.Empresa 
	WHERE Universidad = @Universidad

	SET @TotalMuestra = (SELECT COUNT(DISTINCT Nombre) FROM #Egresados)

    SELECT Rol, COUNT(*)*100/@TotalMuestra AS 'Porcentaje' FROM #Egresados
	GROUP BY Rol
END
GO

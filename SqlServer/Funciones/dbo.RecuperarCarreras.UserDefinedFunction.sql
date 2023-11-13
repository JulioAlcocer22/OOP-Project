/****** Object:  UserDefinedFunction [dbo].[RecuperarCarreras]    Script Date: 12/11/2023 05:36:02 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE FUNCTION [dbo].[RecuperarCarreras]
(
@Universidad VARCHAR(255)
)
RETURNS TABLE 
AS
RETURN 
(
	SELECT DISTINCT Carrera FROM dbo.EgresadoInfo WHERE Universidad = @Universidad
)
GO

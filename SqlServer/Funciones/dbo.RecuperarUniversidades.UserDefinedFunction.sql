/****** Object:  UserDefinedFunction [dbo].[RecuperarUniversidades]    Script Date: 12/11/2023 05:36:02 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE FUNCTION [dbo].[RecuperarUniversidades]
(
)
RETURNS TABLE 
AS
RETURN 
(
	SELECT DISTINCT Universidad FROM dbo.EgresadoInfo
)
GO

USE [master]
GO
/****** Object:  Database [human_resource]    Script Date: 23/03/2025 04:41:28 ******/
CREATE DATABASE [human_resource]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'human_resource', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL12.MSSQLSERVER\MSSQL\DATA\human_resource.mdf' , SIZE = 4510720KB , MAXSIZE = UNLIMITED, FILEGROWTH = 1024KB )
 LOG ON 
( NAME = N'human_resource_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL12.MSSQLSERVER\MSSQL\DATA\human_resource_log.ldf' , SIZE = 1785856KB , MAXSIZE = 2048GB , FILEGROWTH = 10%)
GO
ALTER DATABASE [human_resource] SET COMPATIBILITY_LEVEL = 120
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [human_resource].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [human_resource] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [human_resource] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [human_resource] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [human_resource] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [human_resource] SET ARITHABORT OFF 
GO
ALTER DATABASE [human_resource] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [human_resource] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [human_resource] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [human_resource] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [human_resource] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [human_resource] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [human_resource] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [human_resource] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [human_resource] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [human_resource] SET  DISABLE_BROKER 
GO
ALTER DATABASE [human_resource] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [human_resource] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [human_resource] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [human_resource] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [human_resource] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [human_resource] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [human_resource] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [human_resource] SET RECOVERY FULL 
GO
ALTER DATABASE [human_resource] SET  MULTI_USER 
GO
ALTER DATABASE [human_resource] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [human_resource] SET DB_CHAINING OFF 
GO
ALTER DATABASE [human_resource] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [human_resource] SET TARGET_RECOVERY_TIME = 0 SECONDS 
GO
ALTER DATABASE [human_resource] SET DELAYED_DURABILITY = DISABLED 
GO
EXEC sys.sp_db_vardecimal_storage_format N'human_resource', N'ON'
GO
USE [human_resource]
GO
/****** Object:  Table [dbo].[Employees]    Script Date: 23/03/2025 04:41:28 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[Employees](
	[EmployeeID] [int] NOT NULL,
	[FirstName] [varchar](50) NOT NULL,
	[LastName] [varchar](50) NOT NULL,
	[ManagerID] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[EmployeeID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[hr_1m]    Script Date: 23/03/2025 04:41:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[hr_1m](
	[Emp ID] [varchar](50) NULL,
	[Name Prefix] [varchar](50) NULL,
	[First Name] [varchar](50) NULL,
	[Middle Initial] [varchar](50) NULL,
	[Last Name] [varchar](50) NULL,
	[Gender] [varchar](50) NULL,
	[E Mail] [varchar](50) NULL,
	[Father's Name] [varchar](50) NULL,
	[Mother's Name] [varchar](50) NULL,
	[Mother's Maiden Name] [varchar](50) NULL,
	[Date of Birth] [varchar](50) NULL,
	[Time of Birth] [varchar](50) NULL,
	[Age in Yrs ] [varchar](50) NULL,
	[Weight in Kgs ] [varchar](50) NULL,
	[Date of Joining] [varchar](50) NULL,
	[Quarter of Joining] [varchar](50) NULL,
	[Half of Joining] [varchar](50) NULL,
	[Year of Joining] [varchar](50) NULL,
	[Month of Joining] [varchar](50) NULL,
	[Month Name of Joining] [varchar](50) NULL,
	[Short Month] [varchar](50) NULL,
	[Day of Joining] [varchar](50) NULL,
	[DOW of Joining] [varchar](50) NULL,
	[Short DOW] [varchar](50) NULL,
	[Age in Company (Years)] [varchar](50) NULL,
	[Salary] [varchar](50) NULL,
	[Last % Hike] [varchar](50) NULL,
	[SSN] [varchar](50) NULL,
	[Phone No  ] [varchar](50) NULL,
	[Place Name] [varchar](50) NULL,
	[County] [varchar](50) NULL,
	[City] [varchar](50) NULL,
	[State] [varchar](50) NULL,
	[Zip] [varchar](50) NULL,
	[Region] [varchar](50) NULL,
	[User Name] [varchar](50) NULL,
	[Password] [varchar](50) NULL
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[hr_1m_clean]    Script Date: 23/03/2025 04:41:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[hr_1m_clean](
	[emp_id] [int] NULL,
	[prefix] [varchar](50) NULL
) ON [PRIMARY]
SET ANSI_PADDING OFF
ALTER TABLE [dbo].[hr_1m_clean] ADD [employee_name] [varchar](152) NOT NULL
SET ANSI_PADDING ON
ALTER TABLE [dbo].[hr_1m_clean] ADD [maiden_name] [varchar](50) NULL
ALTER TABLE [dbo].[hr_1m_clean] ADD [gender] [varchar](50) NULL
ALTER TABLE [dbo].[hr_1m_clean] ADD [dob] [date] NULL
ALTER TABLE [dbo].[hr_1m_clean] ADD [birth_time] [time](7) NULL
ALTER TABLE [dbo].[hr_1m_clean] ADD [weight_kgs] [decimal](10, 1) NULL
ALTER TABLE [dbo].[hr_1m_clean] ADD [join_date] [date] NULL
ALTER TABLE [dbo].[hr_1m_clean] ADD [half_yr_joined] [varchar](50) NULL
ALTER TABLE [dbo].[hr_1m_clean] ADD [quarter_joined] [varchar](50) NULL
ALTER TABLE [dbo].[hr_1m_clean] ADD [month_joined] [int] NULL
ALTER TABLE [dbo].[hr_1m_clean] ADD [month_joined_name] [varchar](50) NULL
ALTER TABLE [dbo].[hr_1m_clean] ADD [age_in_company_yrs] [decimal](10, 2) NULL
ALTER TABLE [dbo].[hr_1m_clean] ADD [join_year] [int] NULL
ALTER TABLE [dbo].[hr_1m_clean] ADD [ssn] [varchar](50) NULL
ALTER TABLE [dbo].[hr_1m_clean] ADD [phone] [varchar](50) NULL
ALTER TABLE [dbo].[hr_1m_clean] ADD [email] [varchar](50) NULL
ALTER TABLE [dbo].[hr_1m_clean] ADD [place] [varchar](50) NULL
ALTER TABLE [dbo].[hr_1m_clean] ADD [county] [varchar](50) NULL
ALTER TABLE [dbo].[hr_1m_clean] ADD [city] [varchar](50) NULL
ALTER TABLE [dbo].[hr_1m_clean] ADD [state] [varchar](50) NULL
ALTER TABLE [dbo].[hr_1m_clean] ADD [zipcode] [int] NULL
ALTER TABLE [dbo].[hr_1m_clean] ADD [region] [varchar](50) NULL
ALTER TABLE [dbo].[hr_1m_clean] ADD [salary] [decimal](10, 2) NULL

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[hr_2m]    Script Date: 23/03/2025 04:41:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[hr_2m](
	[Emp ID] [varchar](50) NULL,
	[Name Prefix] [varchar](50) NULL,
	[First Name] [varchar](50) NULL,
	[Middle Initial] [varchar](50) NULL,
	[Last Name] [varchar](50) NULL,
	[Gender] [varchar](50) NULL,
	[E Mail] [varchar](50) NULL,
	[Father's Name] [varchar](50) NULL,
	[Mother's Name] [varchar](50) NULL,
	[Mother's Maiden Name] [varchar](50) NULL,
	[Date of Birth] [varchar](50) NULL,
	[Time of Birth] [varchar](50) NULL,
	[Age in Yrs ] [varchar](50) NULL,
	[Weight in Kgs ] [varchar](50) NULL,
	[Date of Joining] [varchar](50) NULL,
	[Quarter of Joining] [varchar](50) NULL,
	[Half of Joining] [varchar](50) NULL,
	[Year of Joining] [varchar](50) NULL,
	[Month of Joining] [varchar](50) NULL,
	[Month Name of Joining] [varchar](50) NULL,
	[Short Month] [varchar](50) NULL,
	[Day of Joining] [varchar](50) NULL,
	[DOW of Joining] [varchar](50) NULL,
	[Short DOW] [varchar](50) NULL,
	[Age in Company (Years)] [varchar](50) NULL,
	[Salary] [varchar](50) NULL,
	[Last % Hike] [varchar](50) NULL,
	[SSN] [varchar](50) NULL,
	[Phone No  ] [varchar](50) NULL,
	[Place Name] [varchar](50) NULL,
	[County] [varchar](50) NULL,
	[City] [varchar](50) NULL,
	[State] [varchar](50) NULL,
	[Zip] [varchar](50) NULL,
	[Region] [varchar](50) NULL,
	[User Name] [varchar](50) NULL,
	[Password] [varchar](50) NULL
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[hr_2m_clean]    Script Date: 23/03/2025 04:41:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[hr_2m_clean](
	[emp_id] [int] NULL,
	[prefix] [varchar](50) NULL
) ON [PRIMARY]
SET ANSI_PADDING OFF
ALTER TABLE [dbo].[hr_2m_clean] ADD [employee_name] [varchar](152) NOT NULL
SET ANSI_PADDING ON
ALTER TABLE [dbo].[hr_2m_clean] ADD [maiden_name] [varchar](50) NULL
ALTER TABLE [dbo].[hr_2m_clean] ADD [gender] [varchar](50) NULL
ALTER TABLE [dbo].[hr_2m_clean] ADD [dob] [date] NULL
ALTER TABLE [dbo].[hr_2m_clean] ADD [birth_time] [time](7) NULL
ALTER TABLE [dbo].[hr_2m_clean] ADD [weight_kgs] [decimal](10, 1) NULL
ALTER TABLE [dbo].[hr_2m_clean] ADD [join_date] [date] NULL
ALTER TABLE [dbo].[hr_2m_clean] ADD [half_yr_joined] [varchar](50) NULL
ALTER TABLE [dbo].[hr_2m_clean] ADD [quarter_joined] [varchar](50) NULL
ALTER TABLE [dbo].[hr_2m_clean] ADD [month_joined] [int] NULL
ALTER TABLE [dbo].[hr_2m_clean] ADD [month_joined_name] [varchar](50) NULL
ALTER TABLE [dbo].[hr_2m_clean] ADD [age_in_company_yrs] [decimal](10, 2) NULL
ALTER TABLE [dbo].[hr_2m_clean] ADD [join_year] [int] NULL
ALTER TABLE [dbo].[hr_2m_clean] ADD [ssn] [varchar](50) NULL
ALTER TABLE [dbo].[hr_2m_clean] ADD [phone] [varchar](50) NULL
ALTER TABLE [dbo].[hr_2m_clean] ADD [email] [varchar](50) NULL
ALTER TABLE [dbo].[hr_2m_clean] ADD [place] [varchar](50) NULL
ALTER TABLE [dbo].[hr_2m_clean] ADD [county] [varchar](50) NULL
ALTER TABLE [dbo].[hr_2m_clean] ADD [city] [varchar](50) NULL
ALTER TABLE [dbo].[hr_2m_clean] ADD [state] [varchar](50) NULL
ALTER TABLE [dbo].[hr_2m_clean] ADD [zipcode] [int] NULL
ALTER TABLE [dbo].[hr_2m_clean] ADD [region] [varchar](50) NULL
ALTER TABLE [dbo].[hr_2m_clean] ADD [salary] [decimal](10, 2) NULL

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[hr_5m]    Script Date: 23/03/2025 04:41:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[hr_5m](
	[Emp ID] [varchar](50) NULL,
	[Name Prefix] [varchar](50) NULL,
	[First Name] [varchar](50) NULL,
	[Middle Initial] [varchar](50) NULL,
	[Last Name] [varchar](50) NULL,
	[Gender] [varchar](50) NULL,
	[E Mail] [varchar](50) NULL,
	[Father's Name] [varchar](50) NULL,
	[Mother's Name] [varchar](50) NULL,
	[Mother's Maiden Name] [varchar](50) NULL,
	[Date of Birth] [varchar](50) NULL,
	[Time of Birth] [varchar](50) NULL,
	[Age in Yrs ] [varchar](50) NULL,
	[Weight in Kgs ] [varchar](50) NULL,
	[Date of Joining] [varchar](50) NULL,
	[Quarter of Joining] [varchar](50) NULL,
	[Half of Joining] [varchar](50) NULL,
	[Year of Joining] [varchar](50) NULL,
	[Month of Joining] [varchar](50) NULL,
	[Month Name of Joining] [varchar](50) NULL,
	[Short Month] [varchar](50) NULL,
	[Day of Joining] [varchar](50) NULL,
	[DOW of Joining] [varchar](50) NULL,
	[Short DOW] [varchar](50) NULL,
	[Age in Company (Years)] [varchar](50) NULL,
	[Salary] [varchar](50) NULL,
	[Last % Hike] [varchar](50) NULL,
	[SSN] [varchar](50) NULL,
	[Phone No  ] [varchar](50) NULL,
	[Place Name] [varchar](50) NULL,
	[County] [varchar](50) NULL,
	[City] [varchar](50) NULL,
	[State] [varchar](50) NULL,
	[Zip] [varchar](50) NULL,
	[Region] [varchar](50) NULL,
	[User Name] [varchar](50) NULL,
	[Password] [varchar](50) NULL
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[hr_5m_clean]    Script Date: 23/03/2025 04:41:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[hr_5m_clean](
	[emp_id] [int] NULL,
	[prefix] [varchar](50) NULL
) ON [PRIMARY]
SET ANSI_PADDING OFF
ALTER TABLE [dbo].[hr_5m_clean] ADD [employee_name] [varchar](152) NOT NULL
SET ANSI_PADDING ON
ALTER TABLE [dbo].[hr_5m_clean] ADD [maiden_name] [varchar](50) NULL
ALTER TABLE [dbo].[hr_5m_clean] ADD [gender] [varchar](50) NULL
ALTER TABLE [dbo].[hr_5m_clean] ADD [dob] [date] NULL
ALTER TABLE [dbo].[hr_5m_clean] ADD [birth_time] [time](7) NULL
ALTER TABLE [dbo].[hr_5m_clean] ADD [weight_kgs] [decimal](10, 1) NULL
ALTER TABLE [dbo].[hr_5m_clean] ADD [join_date] [date] NULL
ALTER TABLE [dbo].[hr_5m_clean] ADD [half_yr_joined] [varchar](50) NULL
ALTER TABLE [dbo].[hr_5m_clean] ADD [quarter_joined] [varchar](50) NULL
ALTER TABLE [dbo].[hr_5m_clean] ADD [month_joined] [int] NULL
ALTER TABLE [dbo].[hr_5m_clean] ADD [month_joined_name] [varchar](50) NULL
ALTER TABLE [dbo].[hr_5m_clean] ADD [age_in_company_yrs] [decimal](10, 2) NULL
ALTER TABLE [dbo].[hr_5m_clean] ADD [join_year] [int] NULL
ALTER TABLE [dbo].[hr_5m_clean] ADD [ssn] [varchar](50) NULL
ALTER TABLE [dbo].[hr_5m_clean] ADD [phone] [varchar](50) NULL
ALTER TABLE [dbo].[hr_5m_clean] ADD [email] [varchar](50) NULL
ALTER TABLE [dbo].[hr_5m_clean] ADD [place] [varchar](50) NULL
ALTER TABLE [dbo].[hr_5m_clean] ADD [county] [varchar](50) NULL
ALTER TABLE [dbo].[hr_5m_clean] ADD [city] [varchar](50) NULL
ALTER TABLE [dbo].[hr_5m_clean] ADD [state] [varchar](50) NULL
ALTER TABLE [dbo].[hr_5m_clean] ADD [zipcode] [int] NULL
ALTER TABLE [dbo].[hr_5m_clean] ADD [region] [varchar](50) NULL
ALTER TABLE [dbo].[hr_5m_clean] ADD [salary] [decimal](10, 2) NULL

GO
SET ANSI_PADDING OFF
GO
/****** Object:  View [dbo].[employee_age]    Script Date: 23/03/2025 04:41:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE VIEW [dbo].[employee_age] AS 
	SELECT *, (FLOOR(DATEDIFF(YEAR, dob, '2020-12-31'))) AS emp_age 
	FROM hr_1m_clean
	WHERE dob IS NOT NULL;
GO
USE [master]
GO
ALTER DATABASE [human_resource] SET  READ_WRITE 
GO

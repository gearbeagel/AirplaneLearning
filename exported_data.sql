BEGIN TRANSACTION;
CREATE TABLE "account_emailaddress" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "verified" bool NOT NULL, "primary" bool NOT NULL, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "email" varchar(254) NOT NULL);
INSERT INTO "account_emailaddress" VALUES(1,1,1,2,'mnoanyesmai@gmail.com');
INSERT INTO "account_emailaddress" VALUES(2,1,1,3,'kondratskayavictoria@gmail.com');
CREATE TABLE "account_emailconfirmation" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created" datetime NOT NULL, "sent" datetime NULL, "key" varchar(64) NOT NULL UNIQUE, "email_address_id" integer NOT NULL REFERENCES "account_emailaddress" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(150) NOT NULL UNIQUE);
CREATE TABLE "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);
INSERT INTO "auth_permission" VALUES(1,1,'add_logentry','Can add log entry');
INSERT INTO "auth_permission" VALUES(2,1,'change_logentry','Can change log entry');
INSERT INTO "auth_permission" VALUES(3,1,'delete_logentry','Can delete log entry');
INSERT INTO "auth_permission" VALUES(4,1,'view_logentry','Can view log entry');
INSERT INTO "auth_permission" VALUES(5,2,'add_permission','Can add permission');
INSERT INTO "auth_permission" VALUES(6,2,'change_permission','Can change permission');
INSERT INTO "auth_permission" VALUES(7,2,'delete_permission','Can delete permission');
INSERT INTO "auth_permission" VALUES(8,2,'view_permission','Can view permission');
INSERT INTO "auth_permission" VALUES(9,3,'add_group','Can add group');
INSERT INTO "auth_permission" VALUES(10,3,'change_group','Can change group');
INSERT INTO "auth_permission" VALUES(11,3,'delete_group','Can delete group');
INSERT INTO "auth_permission" VALUES(12,3,'view_group','Can view group');
INSERT INTO "auth_permission" VALUES(13,4,'add_user','Can add user');
INSERT INTO "auth_permission" VALUES(14,4,'change_user','Can change user');
INSERT INTO "auth_permission" VALUES(15,4,'delete_user','Can delete user');
INSERT INTO "auth_permission" VALUES(16,4,'view_user','Can view user');
INSERT INTO "auth_permission" VALUES(17,5,'add_contenttype','Can add content type');
INSERT INTO "auth_permission" VALUES(18,5,'change_contenttype','Can change content type');
INSERT INTO "auth_permission" VALUES(19,5,'delete_contenttype','Can delete content type');
INSERT INTO "auth_permission" VALUES(20,5,'view_contenttype','Can view content type');
INSERT INTO "auth_permission" VALUES(21,6,'add_session','Can add session');
INSERT INTO "auth_permission" VALUES(22,6,'change_session','Can change session');
INSERT INTO "auth_permission" VALUES(23,6,'delete_session','Can delete session');
INSERT INTO "auth_permission" VALUES(24,6,'view_session','Can view session');
INSERT INTO "auth_permission" VALUES(25,7,'add_site','Can add site');
INSERT INTO "auth_permission" VALUES(26,7,'change_site','Can change site');
INSERT INTO "auth_permission" VALUES(27,7,'delete_site','Can delete site');
INSERT INTO "auth_permission" VALUES(28,7,'view_site','Can view site');
INSERT INTO "auth_permission" VALUES(29,8,'add_emailaddress','Can add email address');
INSERT INTO "auth_permission" VALUES(30,8,'change_emailaddress','Can change email address');
INSERT INTO "auth_permission" VALUES(31,8,'delete_emailaddress','Can delete email address');
INSERT INTO "auth_permission" VALUES(32,8,'view_emailaddress','Can view email address');
INSERT INTO "auth_permission" VALUES(33,9,'add_emailconfirmation','Can add email confirmation');
INSERT INTO "auth_permission" VALUES(34,9,'change_emailconfirmation','Can change email confirmation');
INSERT INTO "auth_permission" VALUES(35,9,'delete_emailconfirmation','Can delete email confirmation');
INSERT INTO "auth_permission" VALUES(36,9,'view_emailconfirmation','Can view email confirmation');
INSERT INTO "auth_permission" VALUES(37,10,'add_socialaccount','Can add social account');
INSERT INTO "auth_permission" VALUES(38,10,'change_socialaccount','Can change social account');
INSERT INTO "auth_permission" VALUES(39,10,'delete_socialaccount','Can delete social account');
INSERT INTO "auth_permission" VALUES(40,10,'view_socialaccount','Can view social account');
INSERT INTO "auth_permission" VALUES(41,11,'add_socialapp','Can add social application');
INSERT INTO "auth_permission" VALUES(42,11,'change_socialapp','Can change social application');
INSERT INTO "auth_permission" VALUES(43,11,'delete_socialapp','Can delete social application');
INSERT INTO "auth_permission" VALUES(44,11,'view_socialapp','Can view social application');
INSERT INTO "auth_permission" VALUES(45,12,'add_socialtoken','Can add social application token');
INSERT INTO "auth_permission" VALUES(46,12,'change_socialtoken','Can change social application token');
INSERT INTO "auth_permission" VALUES(47,12,'delete_socialtoken','Can delete social application token');
INSERT INTO "auth_permission" VALUES(48,12,'view_socialtoken','Can view social application token');
INSERT INTO "auth_permission" VALUES(49,13,'add_section','Can add section');
INSERT INTO "auth_permission" VALUES(50,13,'change_section','Can change section');
INSERT INTO "auth_permission" VALUES(51,13,'delete_section','Can delete section');
INSERT INTO "auth_permission" VALUES(52,13,'view_section','Can view section');
INSERT INTO "auth_permission" VALUES(53,14,'add_language','Can add language');
INSERT INTO "auth_permission" VALUES(54,14,'change_language','Can change language');
INSERT INTO "auth_permission" VALUES(55,14,'delete_language','Can delete language');
INSERT INTO "auth_permission" VALUES(56,14,'view_language','Can view language');
INSERT INTO "auth_permission" VALUES(57,15,'add_module','Can add module');
INSERT INTO "auth_permission" VALUES(58,15,'change_module','Can change module');
INSERT INTO "auth_permission" VALUES(59,15,'delete_module','Can delete module');
INSERT INTO "auth_permission" VALUES(60,15,'view_module','Can view module');
INSERT INTO "auth_permission" VALUES(61,16,'add_lesson','Can add lesson');
INSERT INTO "auth_permission" VALUES(62,16,'change_lesson','Can change lesson');
INSERT INTO "auth_permission" VALUES(63,16,'delete_lesson','Can delete lesson');
INSERT INTO "auth_permission" VALUES(64,16,'view_lesson','Can view lesson');
INSERT INTO "auth_permission" VALUES(65,17,'add_profile','Can add profile');
INSERT INTO "auth_permission" VALUES(66,17,'change_profile','Can change profile');
INSERT INTO "auth_permission" VALUES(67,17,'delete_profile','Can delete profile');
INSERT INTO "auth_permission" VALUES(68,17,'view_profile','Can view profile');
INSERT INTO "auth_permission" VALUES(69,18,'add_answer','Can add answer');
INSERT INTO "auth_permission" VALUES(70,18,'change_answer','Can change answer');
INSERT INTO "auth_permission" VALUES(71,18,'delete_answer','Can delete answer');
INSERT INTO "auth_permission" VALUES(72,18,'view_answer','Can view answer');
INSERT INTO "auth_permission" VALUES(73,19,'add_question','Can add question');
INSERT INTO "auth_permission" VALUES(74,19,'change_question','Can change question');
INSERT INTO "auth_permission" VALUES(75,19,'delete_question','Can delete question');
INSERT INTO "auth_permission" VALUES(76,19,'view_question','Can view question');
INSERT INTO "auth_permission" VALUES(77,20,'add_quiz','Can add quiz');
INSERT INTO "auth_permission" VALUES(78,20,'change_quiz','Can change quiz');
INSERT INTO "auth_permission" VALUES(79,20,'delete_quiz','Can delete quiz');
INSERT INTO "auth_permission" VALUES(80,20,'view_quiz','Can view quiz');
INSERT INTO "auth_permission" VALUES(81,21,'add_useranswer','Can add user answer');
INSERT INTO "auth_permission" VALUES(82,21,'change_useranswer','Can change user answer');
INSERT INTO "auth_permission" VALUES(83,21,'delete_useranswer','Can delete user answer');
INSERT INTO "auth_permission" VALUES(84,21,'view_useranswer','Can view user answer');
INSERT INTO "auth_permission" VALUES(85,22,'add_quizanswer','Can add quiz answer');
INSERT INTO "auth_permission" VALUES(86,22,'change_quizanswer','Can change quiz answer');
INSERT INTO "auth_permission" VALUES(87,22,'delete_quizanswer','Can delete quiz answer');
INSERT INTO "auth_permission" VALUES(88,22,'view_quizanswer','Can view quiz answer');
INSERT INTO "auth_permission" VALUES(89,23,'add_lessonstatus','Can add lesson status');
INSERT INTO "auth_permission" VALUES(90,23,'change_lessonstatus','Can change lesson status');
INSERT INTO "auth_permission" VALUES(91,23,'delete_lessonstatus','Can delete lesson status');
INSERT INTO "auth_permission" VALUES(92,23,'view_lessonstatus','Can view lesson status');
INSERT INTO "auth_permission" VALUES(93,24,'add_quizstatus','Can add quiz status');
INSERT INTO "auth_permission" VALUES(94,24,'change_quizstatus','Can change quiz status');
INSERT INTO "auth_permission" VALUES(95,24,'delete_quizstatus','Can delete quiz status');
INSERT INTO "auth_permission" VALUES(96,24,'view_quizstatus','Can view quiz status');
INSERT INTO "auth_permission" VALUES(97,25,'add_quizuseranswers','Can add quiz user answers');
INSERT INTO "auth_permission" VALUES(98,25,'change_quizuseranswers','Can change quiz user answers');
INSERT INTO "auth_permission" VALUES(99,25,'delete_quizuseranswers','Can delete quiz user answers');
INSERT INTO "auth_permission" VALUES(100,25,'view_quizuseranswers','Can view quiz user answers');
INSERT INTO "auth_permission" VALUES(101,26,'add_topic','Can add topic');
INSERT INTO "auth_permission" VALUES(102,26,'change_topic','Can change topic');
INSERT INTO "auth_permission" VALUES(103,26,'delete_topic','Can delete topic');
INSERT INTO "auth_permission" VALUES(104,26,'view_topic','Can view topic');
INSERT INTO "auth_permission" VALUES(105,27,'add_post','Can add post');
INSERT INTO "auth_permission" VALUES(106,27,'change_post','Can change post');
INSERT INTO "auth_permission" VALUES(107,27,'delete_post','Can delete post');
INSERT INTO "auth_permission" VALUES(108,27,'view_post','Can view post');
INSERT INTO "auth_permission" VALUES(109,28,'add_comment','Can add comment');
INSERT INTO "auth_permission" VALUES(110,28,'change_comment','Can change comment');
INSERT INTO "auth_permission" VALUES(111,28,'delete_comment','Can delete comment');
INSERT INTO "auth_permission" VALUES(112,28,'view_comment','Can view comment');
CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "first_name" varchar(150) NOT NULL);
INSERT INTO "auth_user" VALUES(1,'pbkdf2_sha256$720000$d9VzZChSeMPalhPjazKpBD$OeCEuHfM8vFlSuyoRMh08xd6DcQuZ6SPLDvF/QMFYUw=','2024-03-26 12:26:05.180925',1,'kondr','Learniniee','',1,1,'2024-03-16 13:53:42.528492','Leari');
INSERT INTO "auth_user" VALUES(2,'!woUx2jxHTUFOfOAlR7kDfrm82GS1ryVvdAn1WqO2','2024-03-21 20:24:16.943363',0,'mai','Ellinskiy','mnoanyesmai@gmail.com',0,1,'2024-03-16 14:06:45.681132','Mai');
INSERT INTO "auth_user" VALUES(3,'!miAKiAyfomxXny2odqk3sc2xfTwOJpiffn5H4AKt','2024-03-23 17:21:59.505173',0,'victoria','Kondratska','kondratskayavictoria@gmail.com',0,1,'2024-03-17 11:21:16.140515','Victoria');
CREATE TABLE "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "discussion_forums_comment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "message" text NOT NULL, "created_at" datetime NOT NULL, "created_by_id" bigint NOT NULL REFERENCES "profile_page_profile" ("id") DEFERRABLE INITIALLY DEFERRED, "post_id" bigint NOT NULL REFERENCES "discussion_forums_post" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "discussion_forums_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "message" text NOT NULL, "created_at" datetime NOT NULL, "created_by_id" bigint NOT NULL REFERENCES "profile_page_profile" ("id") DEFERRABLE INITIALLY DEFERRED, "topic_id" bigint NOT NULL REFERENCES "discussion_forums_topic" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "discussion_forums_topic" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_at" datetime NOT NULL, "starter_id" bigint NOT NULL REFERENCES "profile_page_profile" ("id") DEFERRABLE INITIALLY DEFERRED, "subject_id" bigint NOT NULL REFERENCES "modules_lesson" ("id") DEFERRABLE INITIALLY DEFERRED, "description" text NOT NULL, "title" varchar(50) NOT NULL);
CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "action_time" datetime NOT NULL);
CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);
INSERT INTO "django_content_type" VALUES(1,'admin','logentry');
INSERT INTO "django_content_type" VALUES(2,'auth','permission');
INSERT INTO "django_content_type" VALUES(3,'auth','group');
INSERT INTO "django_content_type" VALUES(4,'auth','user');
INSERT INTO "django_content_type" VALUES(5,'contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES(6,'sessions','session');
INSERT INTO "django_content_type" VALUES(7,'sites','site');
INSERT INTO "django_content_type" VALUES(8,'account','emailaddress');
INSERT INTO "django_content_type" VALUES(9,'account','emailconfirmation');
INSERT INTO "django_content_type" VALUES(10,'socialaccount','socialaccount');
INSERT INTO "django_content_type" VALUES(11,'socialaccount','socialapp');
INSERT INTO "django_content_type" VALUES(12,'socialaccount','socialtoken');
INSERT INTO "django_content_type" VALUES(13,'modules','section');
INSERT INTO "django_content_type" VALUES(14,'modules','language');
INSERT INTO "django_content_type" VALUES(15,'modules','module');
INSERT INTO "django_content_type" VALUES(16,'modules','lesson');
INSERT INTO "django_content_type" VALUES(17,'profile_page','profile');
INSERT INTO "django_content_type" VALUES(18,'modules','answer');
INSERT INTO "django_content_type" VALUES(19,'modules','question');
INSERT INTO "django_content_type" VALUES(20,'modules','quiz');
INSERT INTO "django_content_type" VALUES(21,'modules','useranswer');
INSERT INTO "django_content_type" VALUES(22,'modules','quizanswer');
INSERT INTO "django_content_type" VALUES(23,'modules','lessonstatus');
INSERT INTO "django_content_type" VALUES(24,'modules','quizstatus');
INSERT INTO "django_content_type" VALUES(25,'modules','quizuseranswers');
INSERT INTO "django_content_type" VALUES(26,'discussion_forums','topic');
INSERT INTO "django_content_type" VALUES(27,'discussion_forums','post');
INSERT INTO "django_content_type" VALUES(28,'discussion_forums','comment');
CREATE TABLE "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
INSERT INTO "django_migrations" VALUES(1,'contenttypes','0001_initial','2024-03-16 13:52:55.714593');
INSERT INTO "django_migrations" VALUES(2,'auth','0001_initial','2024-03-16 13:52:55.758605');
INSERT INTO "django_migrations" VALUES(3,'admin','0001_initial','2024-03-16 13:52:55.787353');
INSERT INTO "django_migrations" VALUES(4,'admin','0002_logentry_remove_auto_add','2024-03-16 13:52:55.838630');
INSERT INTO "django_migrations" VALUES(5,'admin','0003_logentry_add_action_flag_choices','2024-03-16 13:52:55.871393');
INSERT INTO "django_migrations" VALUES(6,'contenttypes','0002_remove_content_type_name','2024-03-16 13:52:55.920272');
INSERT INTO "django_migrations" VALUES(7,'auth','0002_alter_permission_name_max_length','2024-03-16 13:52:55.987237');
INSERT INTO "django_migrations" VALUES(8,'auth','0003_alter_user_email_max_length','2024-03-16 13:52:56.007228');
INSERT INTO "django_migrations" VALUES(9,'auth','0004_alter_user_username_opts','2024-03-16 13:52:56.021722');
INSERT INTO "django_migrations" VALUES(10,'auth','0005_alter_user_last_login_null','2024-03-16 13:52:56.051391');
INSERT INTO "django_migrations" VALUES(11,'auth','0006_require_contenttypes_0002','2024-03-16 13:52:56.055870');
INSERT INTO "django_migrations" VALUES(12,'auth','0007_alter_validators_add_error_messages','2024-03-16 13:52:56.073452');
INSERT INTO "django_migrations" VALUES(13,'auth','0008_alter_user_username_max_length','2024-03-16 13:52:56.096867');
INSERT INTO "django_migrations" VALUES(14,'auth','0009_alter_user_last_name_max_length','2024-03-16 13:52:56.116880');
INSERT INTO "django_migrations" VALUES(15,'auth','0010_alter_group_name_max_length','2024-03-16 13:52:56.138301');
INSERT INTO "django_migrations" VALUES(16,'auth','0011_update_proxy_permissions','2024-03-16 13:52:56.158523');
INSERT INTO "django_migrations" VALUES(17,'auth','0012_alter_user_first_name_max_length','2024-03-16 13:52:56.183223');
INSERT INTO "django_migrations" VALUES(18,'sessions','0001_initial','2024-03-16 13:52:56.196539');
INSERT INTO "django_migrations" VALUES(19,'account','0001_initial','2024-03-16 14:05:19.792415');
INSERT INTO "django_migrations" VALUES(20,'account','0002_email_max_length','2024-03-16 14:05:19.811055');
INSERT INTO "django_migrations" VALUES(21,'account','0003_alter_emailaddress_create_unique_verified_email','2024-03-16 14:05:19.835227');
INSERT INTO "django_migrations" VALUES(22,'account','0004_alter_emailaddress_drop_unique_email','2024-03-16 14:05:19.854531');
INSERT INTO "django_migrations" VALUES(23,'account','0005_emailaddress_idx_upper_email','2024-03-16 14:05:19.870059');
INSERT INTO "django_migrations" VALUES(24,'sites','0001_initial','2024-03-16 14:05:19.877709');
INSERT INTO "django_migrations" VALUES(25,'sites','0002_alter_domain_unique','2024-03-16 14:05:19.888306');
INSERT INTO "django_migrations" VALUES(26,'socialaccount','0001_initial','2024-03-16 14:05:19.964695');
INSERT INTO "django_migrations" VALUES(27,'socialaccount','0002_token_max_lengths','2024-03-16 14:05:20.011475');
INSERT INTO "django_migrations" VALUES(28,'socialaccount','0003_extra_data_default_dict','2024-03-16 14:05:20.030488');
INSERT INTO "django_migrations" VALUES(29,'socialaccount','0004_app_provider_id_settings','2024-03-16 14:05:20.067211');
INSERT INTO "django_migrations" VALUES(30,'socialaccount','0005_socialtoken_nullable_app','2024-03-16 14:05:20.089889');
INSERT INTO "django_migrations" VALUES(31,'socialaccount','0006_alter_socialaccount_extra_data','2024-03-16 14:05:20.111146');
INSERT INTO "django_migrations" VALUES(32,'modules','0001_initial','2024-03-16 14:16:45.026539');
INSERT INTO "django_migrations" VALUES(33,'profile_page','0001_initial','2024-03-16 14:16:45.048512');
INSERT INTO "django_migrations" VALUES(34,'profile_page','0002_alter_profile_progress','2024-03-16 14:34:10.659122');
INSERT INTO "django_migrations" VALUES(35,'modules','0002_lesson_lesson_type_alter_lesson_difficulty_level','2024-03-16 22:25:40.823386');
INSERT INTO "django_migrations" VALUES(36,'profile_page','0003_profile_profile_pic_url','2024-03-16 23:02:36.048121');
INSERT INTO "django_migrations" VALUES(37,'profile_page','0004_alter_profile_options_alter_profile_managers_and_more','2024-03-17 11:14:21.384605');
INSERT INTO "django_migrations" VALUES(38,'profile_page','0005_profile_user','2024-03-17 11:40:25.491937');
INSERT INTO "django_migrations" VALUES(39,'profile_page','0006_alter_profile_groups_alter_profile_password_and_more','2024-03-17 11:40:25.553574');
INSERT INTO "django_migrations" VALUES(40,'profile_page','0007_remove_profile_user','2024-03-17 11:55:13.809613');
INSERT INTO "django_migrations" VALUES(41,'profile_page','0008_profile_user','2024-03-17 11:56:40.095489');
INSERT INTO "django_migrations" VALUES(42,'modules','0003_question_answer_lesson_questions','2024-03-17 13:50:33.997497');
INSERT INTO "django_migrations" VALUES(43,'modules','0004_remove_lesson_questions_remove_module_lessons_and_more','2024-03-17 14:25:18.389135');
INSERT INTO "django_migrations" VALUES(44,'modules','0005_remove_lesson_lesson_type','2024-03-17 14:27:43.153981');
INSERT INTO "django_migrations" VALUES(45,'modules','0006_question_quiz_section_lesson','2024-03-17 14:38:54.826648');
INSERT INTO "django_migrations" VALUES(46,'modules','0007_useranswer','2024-03-17 14:52:56.115504');
INSERT INTO "django_migrations" VALUES(47,'modules','0008_delete_useranswer','2024-03-17 16:40:32.576352');
INSERT INTO "django_migrations" VALUES(48,'modules','0009_alter_answer_is_correct','2024-03-17 17:27:33.178734');
INSERT INTO "django_migrations" VALUES(49,'modules','0010_quizanswer','2024-03-18 15:04:50.163368');
INSERT INTO "django_migrations" VALUES(50,'modules','0011_delete_quizanswer','2024-03-18 15:07:50.910485');
INSERT INTO "django_migrations" VALUES(51,'profile_page','0009_profile_learner_type','2024-03-18 15:11:01.493102');
INSERT INTO "django_migrations" VALUES(52,'profile_page','0010_alter_profile_learner_type','2024-03-18 19:31:34.077506');
INSERT INTO "django_migrations" VALUES(53,'profile_page','0011_alter_profile_learner_type_alter_profile_progress','2024-03-21 22:04:04.640535');
INSERT INTO "django_migrations" VALUES(54,'modules','0012_remove_quiz_status_lessonstatus','2024-03-21 22:09:31.412879');
INSERT INTO "django_migrations" VALUES(55,'modules','0013_remove_lesson_status','2024-03-21 22:09:31.430125');
INSERT INTO "django_migrations" VALUES(56,'modules','0014_remove_lessonstatus_quiz_quizstatus','2024-03-21 22:13:34.357554');
INSERT INTO "django_migrations" VALUES(57,'modules','0015_alter_quizstatus_status','2024-03-22 21:17:04.491607');
INSERT INTO "django_migrations" VALUES(58,'modules','0016_lessonstatus_finished_at_quizstatus_finished_at_and_more','2024-03-23 12:25:22.290115');
INSERT INTO "django_migrations" VALUES(59,'modules','0017_quizuseranswers','2024-03-23 15:34:37.723023');
INSERT INTO "django_migrations" VALUES(60,'modules','0018_remove_quizuseranswers_answer','2024-03-23 15:49:53.584665');
INSERT INTO "django_migrations" VALUES(61,'discussion_forums','0001_initial','2024-03-23 18:56:28.297615');
INSERT INTO "django_migrations" VALUES(62,'discussion_forums','0002_topic_description','2024-03-26 07:09:01.054223');
INSERT INTO "django_migrations" VALUES(63,'discussion_forums','0003_topic_title','2024-03-26 11:22:06.318707');
CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
INSERT INTO "django_session" VALUES('12u02bnnlaht2f273nmeix6domiugyo7','.eJxlUMtuhDAQ-5c5I5SEPLm1v1FV0eTBEpWSioS9rPbfFygX2tvIY1u2H4De53WuFtc6xrkmjzXl2X7HOuZQoP94wO8NPZTsE06nAhrACj1VlEjTcSFaJTkxVDTws-R7CnHZJLecb1PcuGvaHShhlHDDuBZMSt0ZoziH52cDRwC7lrjYg8nggjn0X3HeHzhNO9yeMdqDc75L-3ap8X6qLlYjlnHz0Vqb4JwzUmKgDrXghHLkjA2cRBU9SmJw8MyJEJjv6FbNODEMTKIMCvf-_7eLwf5dRTMlhXm-AO2PdRA:1rltVv:ERUVOht9nflUfuC5-W-xz3J4MzOLdvaTmgCyGxiadU8','2024-03-31 16:37:35.793955');
INSERT INTO "django_session" VALUES('6ewj50p6fis9y0jktjfk1mpk2fxqqlh3','.eJwtjEEOgyAQRe8ya9MMgmXgKo0xBImSWKbRoRvj3UvT_tVbvPdPCDFyLTKFKmsqkmOQzGV6Jll5PsA_TvgxeDg45rD9C-ggCHhlFRJhr-83Y5xG23fw2vmd57S3ZGFettTcmr8PCgfCQbeRIu0sGXQGrvH6ALD9KsE:1rmg6W:q0BOV1f6MqcIk_ydiaoXMZc3UmewwH3xh47yUr9PV7Y','2024-04-02 20:30:36.455590');
INSERT INTO "django_session" VALUES('bgcioel69f7sw39jr04bxpj45j9wytbs','.eJwtjEEKgzAQRe8yaykTk-CYq5QiIQYdsJmik27Euzel_au3eO-fEFOSWnSKVddclFNUljI9s64yHxDuJ_wYAhySOG7_AjqICsEMBonQOntzPXnsqYPXLm-e896SRWTZcnMrfx8MekJv28iQHQdyODq4HtcHsLUqwA:1rmg8F:LsZ2D43aAzqm8ONnihxSHn89_MjUYWOX83vUCSvZ5YQ','2024-04-02 20:32:23.434540');
INSERT INTO "django_session" VALUES('vnx32ctw70o28yez5ipucpzbd8475kj9','.eJwtjEEKgzAQRe8yaymTJtExVykiIQYNaKbopBvx7k2pf_UW7_0TfAhcsoy-yBKzpOAlcR63KAtPB7jXCX8GBweH5Ne7gAa8gFOdQiLU1jxajU-itoH3zp80xb0mM_O8xuqW9HtQaAmtriNFuu_IYG_gGq4vsggqxg:1rmg8Q:Hrg8_B2J8rkr585hQ7I7I69kB3DsI6NKShWDzWFYGqQ','2024-04-02 20:32:34.630288');
INSERT INTO "django_session" VALUES('fbplcqvdxqn7t0ocnnzeczo7brr0lszp','.eJwtjEEKgzAQRe8yaykZEpsxVylFQgw6YDNFJ27Euzel_au3eO-fEFOSWnSMVZdclFNUljK-si4y7RAeJ_wYAuySOK7_AjqICgE9GiLjrL-RvyN528F7k4OnvLVkFpnX3NzK3wc0PZnethGSHTw5Mzi4ntcHtDIqzw:1rmg9l:unGC7sNK6GLgoIYJABAi3ePUEwCJXfZ15u_rvULopO4','2024-04-02 20:33:57.883979');
INSERT INTO "django_session" VALUES('5kqzkgmqufbv8tagnkp57ldproagabpx','.eJwtjEEKgzAQRe8yaylJzeAkVylFhhg0YDNFJ27Euzel_au3eO-fwDFKLTpy1SUVzZE1SxlfSReZdgiPE34MAXaJmdd_AR2wQrCDNUQG0d3s3SN67OC9yZGntLVkFpnX1Nyavw_WYHP7NrLU-4Gc8Q6u5_UBsy8qyw:1rmgBe:4KhontDLy_J8-j_HZ4EzaHDJwTmia2m7WYJR5kSUCEY','2024-04-02 20:35:54.131576');
INSERT INTO "django_session" VALUES('l7sl2vmgs4f4bx9jsy05df6e9t0q4qex','.eJxVjEsOgzAMRO-SdYUw-Qh3114kcmxXoKIgNWGFeveGikW7nPdmZjeRtjrFregrzmKuBszllyXip-ZD0LIcuCPmdcu1-3ZOXbpbS5rrzFTnNd_P1d_VRGVqP_2DlIfgHQ5eaMQAvfqAVliTawI8igQIbkSy5AQBwDEgqBWXFMz7A68KO-M:1rp5sT:k20_6i-hj1jU6xtUZKUROfpEx3CIBbP6nsCpsncpa14','2024-04-09 12:26:05.185067');
CREATE TABLE "django_site" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "domain" varchar(100) NOT NULL UNIQUE);
INSERT INTO "django_site" VALUES(1,'example.com','example.com');
CREATE TABLE "modules_answer" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "text" varchar(255) NOT NULL, "question_id" bigint NOT NULL REFERENCES "modules_question" ("id") DEFERRABLE INITIALLY DEFERRED, "is_correct" varchar(15) NOT NULL);
INSERT INTO "modules_answer" VALUES(1,'a) play',1,'Incorrect');
INSERT INTO "modules_answer" VALUES(2,'b) plays',1,'Correct');
INSERT INTO "modules_answer" VALUES(3,'c) playing',1,'Incorrect');
INSERT INTO "modules_answer" VALUES(4,'a) goes',2,'Correct');
INSERT INTO "modules_answer" VALUES(5,'b) go',2,'Incorrect');
INSERT INTO "modules_answer" VALUES(6,'c) going',2,'Incorrect');
INSERT INTO "modules_answer" VALUES(7,'a) love',3,'Correct');
INSERT INTO "modules_answer" VALUES(8,'b) loves',3,'Incorrect');
INSERT INTO "modules_answer" VALUES(9,'c) loving',3,'Incorrect');
CREATE TABLE "modules_language" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "joke" text NOT NULL);
INSERT INTO "modules_language" VALUES(1,'English','Would you like a cup of tea?');
INSERT INTO "modules_language" VALUES(2,'German','Beer-beer-be-e-e-r!');
INSERT INTO "modules_language" VALUES(3,'Spanish','Let''s have a nap, then get to work!');
CREATE TABLE "modules_lesson" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "description" text NOT NULL, "module_id" bigint NOT NULL REFERENCES "modules_module" ("id") DEFERRABLE INITIALLY DEFERRED, "difficulty_level" varchar(20) NOT NULL);
INSERT INTO "modules_lesson" VALUES(1,'Present Simple','Here, you''ll learn about Present Simple.',1,'Easy');
INSERT INTO "modules_lesson" VALUES(2,'Conditionals','Here, you''ll learn about Conditionals.',2,'Medium');
CREATE TABLE "modules_lesson_sections" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "lesson_id" bigint NOT NULL REFERENCES "modules_lesson" ("id") DEFERRABLE INITIALLY DEFERRED, "section_id" bigint NOT NULL REFERENCES "modules_section" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "modules_lessonstatus" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "status" varchar(20) NOT NULL, "lesson_id" bigint NOT NULL REFERENCES "modules_lesson" ("id") DEFERRABLE INITIALLY DEFERRED, "profile_id" bigint NOT NULL REFERENCES "profile_page_profile" ("id") DEFERRABLE INITIALLY DEFERRED, "finished_at" datetime NOT NULL);
INSERT INTO "modules_lessonstatus" VALUES(2,'Completed',2,2,'2024-03-26 14:21:21.893254');
INSERT INTO "modules_lessonstatus" VALUES(3,'Completed',1,2,'2024-03-23 20:22:40.357627');
CREATE TABLE "modules_module" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "description" text NOT NULL, "order" integer unsigned NOT NULL CHECK ("order" >= 0), "language_id" bigint NOT NULL REFERENCES "modules_language" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "modules_module" VALUES(1,'Present Simple and Present Continuous','In this module, you are going to learn the difference between Present Simple and Present Continuous.',1,1);
INSERT INTO "modules_module" VALUES(2,'Conditional Sentences','In this module, you are going to learn about Conditionals.',2,1);
CREATE TABLE "modules_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "text" varchar(255) NOT NULL, "quiz_id" bigint NOT NULL REFERENCES "modules_quiz" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "modules_question" VALUES(1,'Choose the correct form of the verb for the sentence: "He ___ tennis every Sunday."',1);
INSERT INTO "modules_question" VALUES(2,'Choose the correct form of the verb for the sentence: "She ___ to the gym every morning before work."',1);
INSERT INTO "modules_question" VALUES(3,'Choose the correct form of the verb for the sentence: "Cats ___ milk."',1);
CREATE TABLE "modules_quiz" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "description" text NOT NULL, "difficulty_level" varchar(20) NOT NULL, "module_id" bigint NOT NULL REFERENCES "modules_module" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "modules_quiz" VALUES(1,'Present Simple','Test your knowledge on Present Simple.','Easy',1);
CREATE TABLE "modules_quiz_questions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "quiz_id" bigint NOT NULL REFERENCES "modules_quiz" ("id") DEFERRABLE INITIALLY DEFERRED, "question_id" bigint NOT NULL REFERENCES "modules_question" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "modules_quizstatus" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "status" varchar(20) NOT NULL, "profile_id" bigint NOT NULL REFERENCES "profile_page_profile" ("id") DEFERRABLE INITIALLY DEFERRED, "quiz_id" bigint NOT NULL REFERENCES "modules_quiz" ("id") DEFERRABLE INITIALLY DEFERRED, "finished_at" datetime NOT NULL);
INSERT INTO "modules_quizstatus" VALUES(1,'Completed',2,1,'2024-03-23 17:44:43.450144');
CREATE TABLE "modules_quizuseranswers" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_answer" text NOT NULL, "is_correct" varchar(15) NOT NULL, "profile_id" bigint NOT NULL REFERENCES "profile_page_profile" ("id") DEFERRABLE INITIALLY DEFERRED, "question_id" bigint NOT NULL REFERENCES "modules_question" ("id") DEFERRABLE INITIALLY DEFERRED, "quiz_id" bigint NOT NULL REFERENCES "modules_quiz" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "modules_quizuseranswers" VALUES(67,'b) go','Incorrect',2,2,1);
INSERT INTO "modules_quizuseranswers" VALUES(68,'b) plays','Correct',2,1,1);
INSERT INTO "modules_quizuseranswers" VALUES(69,'a) love','Correct',2,3,1);
CREATE TABLE "modules_section" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "contents" text NOT NULL, "lesson_id" bigint NOT NULL REFERENCES "modules_lesson" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "modules_section" VALUES(1,'Introduction to Present Simple','In this module, we will explore the present simple tense in English. The present simple tense is one of the most fundamental tenses in English grammar.',1);
INSERT INTO "modules_section" VALUES(2,'What is Present Simple?','<p>
    The present simple tense is used to describe habitual actions, general truths, and scheduled events that occur regularly or repeatedly.
</p>
<p>
    It is formed using the base form of the verb (e.g., eat, sleep, work) with the addition of <strong>''-s''</strong> or <strong>''-es''</strong> for third-person singular subjects (he, she, it).
</p>
<p>
    However, there is one exception that you need to remember: the verb "to be" changes differently:
</p>
<ul>
    <li>I - am</li>
    <li>He, She, It - is</li>
    <li>We, You, They - are</li>
</ul>
',1);
INSERT INTO "modules_section" VALUES(3,'When Do We Use It?','<ul>
        <li><strong>Habitual Actions:</strong> We use the present simple to describe actions that are routine or habitual, such as daily routines, hobbies, or regular activities.</li>
        <li><strong>General Truths:</strong> The present simple is used to express general truths, facts, or statements that are always true.</li>
        <li><strong>Scheduled Events:</strong> It is also used to describe future events that are part of a timetable or schedule, such as public transport timetables or event schedules.</li>
    </ul>',1);
INSERT INTO "modules_section" VALUES(4,'How Do We Use It?','<p>To form the present simple tense, use the base form of the verb for most subjects. For third-person singular subjects (he, she, it), add ''-s'' or ''-es'' to the base form of the verb. </p>
<p>Negative and question forms are created using auxiliary verbs (do/does) followed by the base form of the main verb.</p>
',1);
INSERT INTO "modules_section" VALUES(5,'Examples','<p>Habitual Actions:</p>
<ul>
    <li>I drink coffee every morning.</li>
    <li>She reads a book before bedtime.</li>
    <li>They play soccer every weekend.</li>
</ul>
<p>General Truths:</p>
<ul>
    <li>The sun rises in the east.</li>
    <li>Water boils at 100 degrees Celsius.</li>
    <li>Birds fly.</li>
</ul>
<p>Scheduled Events:</p>
<ul>
    <li>The train departs at 9:00 AM.</li>
    <li>The movie starts at 7:30 PM.</li>
    <li>The concert ends at midnight.</li>
</ul>
',1);
INSERT INTO "modules_section" VALUES(6,'What are Conditionals?','<p>Conditionals in English grammar are structures that express relationships between conditions and their consequences.</p> 
<p>They allow us to talk about hypothetical situations and their potential outcomes. Conditionals consist of two main parts: the condition (the if-clause) and the consequence (the result clause).</p>',2);
INSERT INTO "modules_section" VALUES(7,'Zero Conditional','<ul>
        <li><strong>Used to express general truths, facts, or scientific laws.</strong></li>
        <li><strong>Structure:</strong> If + present simple, present simple.</li>
        <li><strong>Example:</strong> If you heat ice, it melts.</li>
    </ul>',2);
INSERT INTO "modules_section" VALUES(8,'First Conditional','<ul>
        <li><strong>Used to talk about real or possible future situations.</strong></li>
        <li><strong>Structure:</strong> If + present simple, will + base form.</li>
        <li><strong>Example:</strong> If it rains tomorrow, we will stay indoors.</li>
    </ul>',2);
INSERT INTO "modules_section" VALUES(9,'Second Conditional','<ul>
        <li><strong>Used to talk about hypothetical or unreal present or future situations.</strong></li>
        <li><strong>Structure:</strong> If + past simple, would + base form.</li>
        <li><strong>Example:</strong> If I won the lottery, I would travel around the world.</li>
    </ul>',2);
INSERT INTO "modules_section" VALUES(10,'Third Conditional','<ul>
        <li><strong>Used to talk about unreal past situations and their imagined consequences.</strong></li>
        <li><strong>Structure:</strong> If + past perfect, would have + past participle.</li>
        <li><strong>Example:</strong> If she had studied harder, she would have passed the exam.</li>
    </ul>',2);
CREATE TABLE "profile_page_profile" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "profile_pic_url" varchar(200) NOT NULL, "date_joined" datetime NOT NULL, "email" varchar(254) NOT NULL, "first_name" varchar(150) NOT NULL, "is_active" bool NOT NULL, "is_staff" bool NOT NULL, "is_superuser" bool NOT NULL, "last_login" datetime NULL, "last_name" varchar(150) NOT NULL, "password" varchar(128) NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "learner_type" varchar(30) NOT NULL, "progress" real NOT NULL);
INSERT INTO "profile_page_profile" VALUES(1,'/static/plushik_flower.png','2024-03-17 11:56:46.278686','','',1,0,0,NULL,'','','mai',2,'A smart cookie!',100.0);
INSERT INTO "profile_page_profile" VALUES(2,'/static/plushik_knife.png','2024-03-19 12:44:51.985946','','',1,0,0,NULL,'','','',3,'A smart cookie!',100.0);
INSERT INTO "profile_page_profile" VALUES(3,'/static/leeri_logo.png','2024-03-23 17:21:49.452307','','',1,0,0,NULL,'','','kondr',1,'An avid learner!',0.0);
CREATE TABLE "profile_page_profile_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "profile_id" bigint NOT NULL REFERENCES "profile_page_profile" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "profile_page_profile_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "profile_id" bigint NOT NULL REFERENCES "profile_page_profile" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "socialaccount_socialaccount" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "provider" varchar(200) NOT NULL, "uid" varchar(191) NOT NULL, "last_login" datetime NOT NULL, "date_joined" datetime NOT NULL, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "extra_data" text NOT NULL CHECK ((JSON_VALID("extra_data") OR "extra_data" IS NULL)));
INSERT INTO "socialaccount_socialaccount" VALUES(1,'google','102104924852668399744','2024-03-21 20:24:16.918377','2024-03-16 14:06:45.702935',2,'{"iss": "https://accounts.google.com", "azp": "92021185036-ija2gcsktesrejq05st3mrst2p8vn6p8.apps.googleusercontent.com", "aud": "92021185036-ija2gcsktesrejq05st3mrst2p8vn6p8.apps.googleusercontent.com", "sub": "102104924852668399744", "email": "mnoanyesmai@gmail.com", "email_verified": true, "at_hash": "WtTSxSG565p3JFKxNzjWLw", "name": "Mai Ellinskiy", "picture": "https://lh3.googleusercontent.com/a/ACg8ocKN0rvzdEmLGSHsXiUMbEMLFipkwxhbKfIPjY0ghz98=s96-c", "given_name": "Mai", "family_name": "Ellinskiy", "iat": 1711052657, "exp": 1711056257}');
INSERT INTO "socialaccount_socialaccount" VALUES(2,'google','105805333381839784094','2024-03-23 17:21:59.490761','2024-03-17 11:21:16.157150',3,'{"iss": "https://accounts.google.com", "azp": "92021185036-ija2gcsktesrejq05st3mrst2p8vn6p8.apps.googleusercontent.com", "aud": "92021185036-ija2gcsktesrejq05st3mrst2p8vn6p8.apps.googleusercontent.com", "sub": "105805333381839784094", "email": "kondratskayavictoria@gmail.com", "email_verified": true, "at_hash": "p5OZFTM4atNl3_Ecbqq4Fw", "name": "Victoria \u201cVic\u201d Kondratska", "picture": "https://lh3.googleusercontent.com/a/ACg8ocJFJZNoVYEGcGmOpVqBrQLQ4MMWSpmFnx62wtJ4nuWkGQ=s96-c", "given_name": "Victoria", "family_name": "Kondratska", "iat": 1711214518, "exp": 1711218118}');
CREATE TABLE "socialaccount_socialapp" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "provider" varchar(30) NOT NULL, "name" varchar(40) NOT NULL, "client_id" varchar(191) NOT NULL, "secret" varchar(191) NOT NULL, "key" varchar(191) NOT NULL, "provider_id" varchar(200) NOT NULL, "settings" text NOT NULL CHECK ((JSON_VALID("settings") OR "settings" IS NULL)));
CREATE TABLE "socialaccount_socialapp_sites" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "socialapp_id" integer NOT NULL REFERENCES "socialaccount_socialapp" ("id") DEFERRABLE INITIALLY DEFERRED, "site_id" integer NOT NULL REFERENCES "django_site" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "socialaccount_socialtoken" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "token" text NOT NULL, "token_secret" text NOT NULL, "expires_at" datetime NULL, "account_id" integer NOT NULL REFERENCES "socialaccount_socialaccount" ("id") DEFERRABLE INITIALLY DEFERRED, "app_id" integer NULL REFERENCES "socialaccount_socialapp" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id");
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id");
CREATE UNIQUE INDEX "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" ("user_id", "group_id");
CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id");
CREATE UNIQUE INDEX "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" ("user_id", "permission_id");
CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id");
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id");
CREATE UNIQUE INDEX "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model");
CREATE UNIQUE INDEX "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename");
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id");
CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date");
CREATE INDEX "account_emailconfirmation_email_address_id_5b7f8c58" ON "account_emailconfirmation" ("email_address_id");
CREATE UNIQUE INDEX "account_emailaddress_user_id_email_987c8728_uniq" ON "account_emailaddress" ("user_id", "email");
CREATE UNIQUE INDEX "unique_verified_email" ON "account_emailaddress" ("email") WHERE "verified";
CREATE INDEX "account_emailaddress_user_id_2c513194" ON "account_emailaddress" ("user_id");
CREATE INDEX "account_emailaddress_upper" ON "account_emailaddress" ((UPPER("email")));
CREATE UNIQUE INDEX "socialaccount_socialapp_sites_socialapp_id_site_id_71a9a768_uniq" ON "socialaccount_socialapp_sites" ("socialapp_id", "site_id");
CREATE INDEX "socialaccount_socialapp_sites_socialapp_id_97fb6e7d" ON "socialaccount_socialapp_sites" ("socialapp_id");
CREATE INDEX "socialaccount_socialapp_sites_site_id_2579dee5" ON "socialaccount_socialapp_sites" ("site_id");
CREATE UNIQUE INDEX "socialaccount_socialtoken_app_id_account_id_fca4e0ac_uniq" ON "socialaccount_socialtoken" ("app_id", "account_id");
CREATE INDEX "socialaccount_socialtoken_account_id_951f210e" ON "socialaccount_socialtoken" ("account_id");
CREATE INDEX "socialaccount_socialtoken_app_id_636a42d7" ON "socialaccount_socialtoken" ("app_id");
CREATE UNIQUE INDEX "socialaccount_socialaccount_provider_uid_fc810c6e_uniq" ON "socialaccount_socialaccount" ("provider", "uid");
CREATE INDEX "socialaccount_socialaccount_user_id_8146e70c" ON "socialaccount_socialaccount" ("user_id");
CREATE INDEX "modules_module_language_id_593f1691" ON "modules_module" ("language_id");
CREATE UNIQUE INDEX "modules_lesson_sections_lesson_id_section_id_f72bd90e_uniq" ON "modules_lesson_sections" ("lesson_id", "section_id");
CREATE INDEX "modules_lesson_sections_lesson_id_810312c1" ON "modules_lesson_sections" ("lesson_id");
CREATE INDEX "modules_lesson_sections_section_id_fe297b29" ON "modules_lesson_sections" ("section_id");
CREATE INDEX "modules_lesson_module_id_f98fa0c0" ON "modules_lesson" ("module_id");
CREATE UNIQUE INDEX "profile_page_profile_groups_profile_id_group_id_349d5205_uniq" ON "profile_page_profile_groups" ("profile_id", "group_id");
CREATE INDEX "profile_page_profile_groups_profile_id_f2f9258e" ON "profile_page_profile_groups" ("profile_id");
CREATE INDEX "profile_page_profile_groups_group_id_39ee9ee5" ON "profile_page_profile_groups" ("group_id");
CREATE UNIQUE INDEX "profile_page_profile_user_permissions_profile_id_permission_id_9f8ac12c_uniq" ON "profile_page_profile_user_permissions" ("profile_id", "permission_id");
CREATE INDEX "profile_page_profile_user_permissions_profile_id_59348997" ON "profile_page_profile_user_permissions" ("profile_id");
CREATE INDEX "profile_page_profile_user_permissions_permission_id_7834111c" ON "profile_page_profile_user_permissions" ("permission_id");
CREATE INDEX "modules_quiz_module_id_9fbf4b3a" ON "modules_quiz" ("module_id");
CREATE UNIQUE INDEX "modules_quiz_questions_quiz_id_question_id_0834e603_uniq" ON "modules_quiz_questions" ("quiz_id", "question_id");
CREATE INDEX "modules_quiz_questions_quiz_id_46c4770c" ON "modules_quiz_questions" ("quiz_id");
CREATE INDEX "modules_quiz_questions_question_id_562ef272" ON "modules_quiz_questions" ("question_id");
CREATE INDEX "modules_question_quiz_id_d28cf52c" ON "modules_question" ("quiz_id");
CREATE INDEX "modules_section_lesson_id_c5b160c3" ON "modules_section" ("lesson_id");
CREATE INDEX "modules_answer_question_id_a03abd7c" ON "modules_answer" ("question_id");
CREATE INDEX "modules_lessonstatus_lesson_id_1e92e13f" ON "modules_lessonstatus" ("lesson_id");
CREATE INDEX "modules_lessonstatus_profile_id_794379ab" ON "modules_lessonstatus" ("profile_id");
CREATE INDEX "modules_quizstatus_profile_id_f137c6c9" ON "modules_quizstatus" ("profile_id");
CREATE INDEX "modules_quizstatus_quiz_id_70b3da8b" ON "modules_quizstatus" ("quiz_id");
CREATE INDEX "modules_quizuseranswers_profile_id_710b46fc" ON "modules_quizuseranswers" ("profile_id");
CREATE INDEX "modules_quizuseranswers_question_id_5311b09e" ON "modules_quizuseranswers" ("question_id");
CREATE INDEX "modules_quizuseranswers_quiz_id_4c509146" ON "modules_quizuseranswers" ("quiz_id");
CREATE INDEX "discussion_forums_comment_created_by_id_7ba8f179" ON "discussion_forums_comment" ("created_by_id");
CREATE INDEX "discussion_forums_comment_post_id_47b61461" ON "discussion_forums_comment" ("post_id");
CREATE INDEX "discussion_forums_post_created_by_id_69c84e2a" ON "discussion_forums_post" ("created_by_id");
CREATE INDEX "discussion_forums_post_topic_id_fbe2ac9b" ON "discussion_forums_post" ("topic_id");
CREATE INDEX "discussion_forums_topic_starter_id_6a985d69" ON "discussion_forums_topic" ("starter_id");
CREATE INDEX "discussion_forums_topic_subject_id_beab7f9d" ON "discussion_forums_topic" ("subject_id");
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('django_migrations',63);
INSERT INTO "sqlite_sequence" VALUES('django_admin_log',0);
INSERT INTO "sqlite_sequence" VALUES('django_content_type',28);
INSERT INTO "sqlite_sequence" VALUES('auth_permission',112);
INSERT INTO "sqlite_sequence" VALUES('auth_group',0);
INSERT INTO "sqlite_sequence" VALUES('auth_user',3);
INSERT INTO "sqlite_sequence" VALUES('account_emailaddress',2);
INSERT INTO "sqlite_sequence" VALUES('django_site',1);
INSERT INTO "sqlite_sequence" VALUES('socialaccount_socialapp',0);
INSERT INTO "sqlite_sequence" VALUES('socialaccount_socialtoken',0);
INSERT INTO "sqlite_sequence" VALUES('socialaccount_socialaccount',2);
INSERT INTO "sqlite_sequence" VALUES('modules_language',3);
INSERT INTO "sqlite_sequence" VALUES('modules_module',2);
INSERT INTO "sqlite_sequence" VALUES('modules_lesson',2);
INSERT INTO "sqlite_sequence" VALUES('modules_quiz',1);
INSERT INTO "sqlite_sequence" VALUES('modules_question',3);
INSERT INTO "sqlite_sequence" VALUES('modules_section',10);
INSERT INTO "sqlite_sequence" VALUES('modules_answer',9);
INSERT INTO "sqlite_sequence" VALUES('profile_page_profile',3);
INSERT INTO "sqlite_sequence" VALUES('modules_lessonstatus',3);
INSERT INTO "sqlite_sequence" VALUES('modules_quizstatus',1);
INSERT INTO "sqlite_sequence" VALUES('modules_quizuseranswers',72);
INSERT INTO "sqlite_sequence" VALUES('discussion_forums_post',0);
INSERT INTO "sqlite_sequence" VALUES('discussion_forums_topic',0);
COMMIT;

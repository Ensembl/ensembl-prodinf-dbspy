"""
Module containing in/out schemas to be used in the main module.
"""

from datetime import datetime
from typing import List, Optional, Union

from pydantic import BaseModel, Field, AnyUrl


class Message(BaseModel):
    msg: str


class HTTPError(BaseModel):
    detail: List[Message]


class Info(BaseModel):
    name: Optional[str] = Field(example="DBSpy")
    server_version: Optional[str] = Field(example="0.0.1")


class TableStatus(BaseModel):
    Name: str
    Engine: Optional[str]
    Version: Optional[int]
    Row_format: Optional[str]
    Rows: Optional[int]
    Avg_row_length: Optional[int]
    Data_length: Optional[int]
    Max_data_length: Optional[int]
    Index_length: Optional[int]
    Data_free: Optional[int]
    Auto_increment: Optional[int]
    Create_time: datetime
    Update_time: Optional[datetime]
    Check_time: Optional[datetime]
    Collation: Optional[str]
    Checksum: Optional[str]
    Create_options: Optional[str]
    Comment: Optional[str]


class TablesStatus(BaseModel):
    self_url: AnyUrl = Field(
        alias="_self",
        example="http://dbspy.example.org/status/table/mysql-server/3306/db_name?table=table_name",
    )
    results: List[TableStatus]


class GlobalStatus(BaseModel):
    Aborted_clients: Optional[int]
    Aborted_connects: Optional[int]
    Binlog_cache_disk_use: Optional[int]
    Binlog_cache_use: Optional[int]
    Binlog_stmt_cache_disk_use: Optional[int]
    Binlog_stmt_cache_use: Optional[int]
    Bytes_received: Optional[int]
    Bytes_sent: Optional[int]
    Com_admin_commands: Optional[int]
    Com_assign_to_keycache: Optional[int]
    Com_alter_db: Optional[int]
    Com_alter_db_upgrade: Optional[int]
    Com_alter_event: Optional[int]
    Com_alter_function: Optional[int]
    Com_alter_procedure: Optional[int]
    Com_alter_server: Optional[int]
    Com_alter_table: Optional[int]
    Com_alter_tablespace: Optional[int]
    Com_alter_user: Optional[int]
    Com_analyze: Optional[int]
    Com_begin: Optional[int]
    Com_binlog: Optional[int]
    Com_call_procedure: Optional[int]
    Com_change_db: Optional[int]
    Com_change_master: Optional[int]
    Com_check: Optional[int]
    Com_checksum: Optional[int]
    Com_commit: Optional[int]
    Com_create_db: Optional[int]
    Com_create_event: Optional[int]
    Com_create_function: Optional[int]
    Com_create_index: Optional[int]
    Com_create_procedure: Optional[int]
    Com_create_server: Optional[int]
    Com_create_table: Optional[int]
    Com_create_trigger: Optional[int]
    Com_create_udf: Optional[int]
    Com_create_user: Optional[int]
    Com_create_view: Optional[int]
    Com_dealloc_sql: Optional[int]
    Com_delete: Optional[int]
    Com_delete_multi: Optional[int]
    Com_do: Optional[int]
    Com_drop_db: Optional[int]
    Com_drop_event: Optional[int]
    Com_drop_function: Optional[int]
    Com_drop_index: Optional[int]
    Com_drop_procedure: Optional[int]
    Com_drop_server: Optional[int]
    Com_drop_table: Optional[int]
    Com_drop_trigger: Optional[int]
    Com_drop_user: Optional[int]
    Com_drop_view: Optional[int]
    Com_empty_query: Optional[int]
    Com_execute_sql: Optional[int]
    Com_flush: Optional[int]
    Com_get_diagnostics: Optional[int]
    Com_grant: Optional[int]
    Com_ha_close: Optional[int]
    Com_ha_open: Optional[int]
    Com_ha_read: Optional[int]
    Com_help: Optional[int]
    Com_insert: Optional[int]
    Com_insert_select: Optional[int]
    Com_install_plugin: Optional[int]
    Com_kill: Optional[int]
    Com_load: Optional[int]
    Com_lock_tables: Optional[int]
    Com_optimize: Optional[int]
    Com_preload_keys: Optional[int]
    Com_prepare_sql: Optional[int]
    Com_purge: Optional[int]
    Com_purge_before_date: Optional[int]
    Com_release_savepoint: Optional[int]
    Com_rename_table: Optional[int]
    Com_rename_user: Optional[int]
    Com_repair: Optional[int]
    Com_replace: Optional[int]
    Com_replace_select: Optional[int]
    Com_reset: Optional[int]
    Com_resignal: Optional[int]
    Com_revoke: Optional[int]
    Com_revoke_all: Optional[int]
    Com_rollback: Optional[int]
    Com_rollback_to_savepoint: Optional[int]
    Com_savepoint: Optional[int]
    Com_select: Optional[int]
    Com_set_option: Optional[int]
    Com_signal: Optional[int]
    Com_show_binlog_events: Optional[int]
    Com_show_binlogs: Optional[int]
    Com_show_charsets: Optional[int]
    Com_show_collations: Optional[int]
    Com_show_create_db: Optional[int]
    Com_show_create_event: Optional[int]
    Com_show_create_func: Optional[int]
    Com_show_create_proc: Optional[int]
    Com_show_create_table: Optional[int]
    Com_show_create_trigger: Optional[int]
    Com_show_databases: Optional[int]
    Com_show_engine_logs: Optional[int]
    Com_show_engine_mutex: Optional[int]
    Com_show_engine_status: Optional[int]
    Com_show_events: Optional[int]
    Com_show_errors: Optional[int]
    Com_show_fields: Optional[int]
    Com_show_function_code: Optional[int]
    Com_show_function_status: Optional[int]
    Com_show_grants: Optional[int]
    Com_show_keys: Optional[int]
    Com_show_master_status: Optional[int]
    Com_show_open_tables: Optional[int]
    Com_show_plugins: Optional[int]
    Com_show_privileges: Optional[int]
    Com_show_procedure_code: Optional[int]
    Com_show_procedure_status: Optional[int]
    Com_show_processlist: Optional[int]
    Com_show_profile: Optional[int]
    Com_show_profiles: Optional[int]
    Com_show_relaylog_events: Optional[int]
    Com_show_slave_hosts: Optional[int]
    Com_show_slave_status: Optional[int]
    Com_show_status: Optional[int]
    Com_show_storage_engines: Optional[int]
    Com_show_table_status: Optional[int]
    Com_show_tables: Optional[int]
    Com_show_triggers: Optional[int]
    Com_show_variables: Optional[int]
    Com_show_warnings: Optional[int]
    Com_slave_start: Optional[int]
    Com_slave_stop: Optional[int]
    Com_stmt_close: Optional[int]
    Com_stmt_execute: Optional[int]
    Com_stmt_fetch: Optional[int]
    Com_stmt_prepare: Optional[int]
    Com_stmt_reprepare: Optional[int]
    Com_stmt_reset: Optional[int]
    Com_stmt_send_long_data: Optional[int]
    Com_truncate: Optional[int]
    Com_uninstall_plugin: Optional[int]
    Com_unlock_tables: Optional[int]
    Com_update: Optional[int]
    Com_update_multi: Optional[int]
    Com_xa_commit: Optional[int]
    Com_xa_end: Optional[int]
    Com_xa_prepare: Optional[int]
    Com_xa_recover: Optional[int]
    Com_xa_rollback: Optional[int]
    Com_xa_start: Optional[int]
    Compression: Optional[str]
    Connection_errors_accept: Optional[int]
    Connection_errors_internal: Optional[int]
    Connection_errors_max_connections: Optional[int]
    Connection_errors_peer_address: Optional[int]
    Connection_errors_select: Optional[int]
    Connection_errors_tcpwrap: Optional[int]
    Connections: Optional[int]
    Created_tmp_disk_tables: Optional[int]
    Created_tmp_files: Optional[int]
    Created_tmp_tables: Optional[int]
    Delayed_errors: Optional[int]
    Delayed_insert_threads: Optional[int]
    Delayed_writes: Optional[int]
    Flush_commands: Optional[int]
    Handler_commit: Optional[int]
    Handler_delete: Optional[int]
    Handler_discover: Optional[int]
    Handler_external_lock: Optional[int]
    Handler_mrr_init: Optional[int]
    Handler_prepare: Optional[int]
    Handler_read_first: Optional[int]
    Handler_read_key: Optional[int]
    Handler_read_last: Optional[int]
    Handler_read_next: Optional[int]
    Handler_read_prev: Optional[int]
    Handler_read_rnd: Optional[int]
    Handler_read_rnd_next: Optional[int]
    Handler_rollback: Optional[int]
    Handler_savepoint: Optional[int]
    Handler_savepoint_rollback: Optional[int]
    Handler_update: Optional[int]
    Handler_write: Optional[int]
    Innodb_buffer_pool_dump_status: Optional[str]
    Innodb_buffer_pool_load_status: Optional[str]
    Innodb_buffer_pool_pages_data: Optional[int]
    Innodb_buffer_pool_bytes_data: Optional[int]
    Innodb_buffer_pool_pages_dirty: Optional[int]
    Innodb_buffer_pool_bytes_dirty: Optional[int]
    Innodb_buffer_pool_pages_flushed: Optional[int]
    Innodb_buffer_pool_pages_free: Optional[int]
    Innodb_buffer_pool_pages_misc: Optional[int]
    Innodb_buffer_pool_pages_total: Optional[int]
    Innodb_buffer_pool_read_ahead_rnd: Optional[int]
    Innodb_buffer_pool_read_ahead: Optional[int]
    Innodb_buffer_pool_read_ahead_evicted: Optional[int]
    Innodb_buffer_pool_read_requests: Optional[int]
    Innodb_buffer_pool_reads: Optional[int]
    Innodb_buffer_pool_wait_free: Optional[int]
    Innodb_buffer_pool_write_requests: Optional[int]
    Innodb_data_fsyncs: Optional[int]
    Innodb_data_pending_fsyncs: Optional[int]
    Innodb_data_pending_reads: Optional[int]
    Innodb_data_pending_writes: Optional[int]
    Innodb_data_read: Optional[int]
    Innodb_data_reads: Optional[int]
    Innodb_data_writes: Optional[int]
    Innodb_data_written: Optional[int]
    Innodb_dblwr_pages_written: Optional[int]
    Innodb_dblwr_writes: Optional[int]
    Innodb_have_atomic_builtins: Optional[str]
    Innodb_log_waits: Optional[int]
    Innodb_log_write_requests: Optional[int]
    Innodb_log_writes: Optional[int]
    Innodb_os_log_fsyncs: Optional[int]
    Innodb_os_log_pending_fsyncs: Optional[int]
    Innodb_os_log_pending_writes: Optional[int]
    Innodb_os_log_written: Optional[int]
    Innodb_page_size: Optional[int]
    Innodb_pages_created: Optional[int]
    Innodb_pages_read: Optional[int]
    Innodb_pages_written: Optional[int]
    Innodb_row_lock_current_waits: Optional[int]
    Innodb_row_lock_time: Optional[int]
    Innodb_row_lock_time_avg: Optional[int]
    Innodb_row_lock_time_max: Optional[int]
    Innodb_row_lock_waits: Optional[int]
    Innodb_rows_deleted: Optional[int]
    Innodb_rows_inserted: Optional[int]
    Innodb_rows_read: Optional[int]
    Innodb_rows_updated: Optional[int]
    Innodb_num_open_files: Optional[int]
    Innodb_truncated_status_writes: Optional[int]
    Innodb_available_undo_logs: Optional[int]
    Key_blocks_not_flushed: Optional[int]
    Key_blocks_unused: Optional[int]
    Key_blocks_used: Optional[int]
    Key_read_requests: Optional[int]
    Key_reads: Optional[int]
    Key_write_requests: Optional[int]
    Key_writes: Optional[int]
    Last_query_cost: Optional[float]
    Last_query_partial_plans: Optional[int]
    Max_used_connections: Optional[int]
    Not_flushed_delayed_rows: Optional[int]
    Open_files: Optional[int]
    Open_streams: Optional[int]
    Open_table_definitions: Optional[int]
    Open_tables: Optional[int]
    Opened_files: Optional[int]
    Opened_table_definitions: Optional[int]
    Opened_tables: Optional[int]
    Performance_schema_accounts_lost: Optional[int]
    Performance_schema_cond_classes_lost: Optional[int]
    Performance_schema_cond_instances_lost: Optional[int]
    Performance_schema_digest_lost: Optional[int]
    Performance_schema_file_classes_lost: Optional[int]
    Performance_schema_file_handles_lost: Optional[int]
    Performance_schema_file_instances_lost: Optional[int]
    Performance_schema_hosts_lost: Optional[int]
    Performance_schema_locker_lost: Optional[int]
    Performance_schema_mutex_classes_lost: Optional[int]
    Performance_schema_mutex_instances_lost: Optional[int]
    Performance_schema_rwlock_classes_lost: Optional[int]
    Performance_schema_rwlock_instances_lost: Optional[int]
    Performance_schema_session_connect_attrs_lost: Optional[int]
    Performance_schema_socket_classes_lost: Optional[int]
    Performance_schema_socket_instances_lost: Optional[int]
    Performance_schema_stage_classes_lost: Optional[int]
    Performance_schema_statement_classes_lost: Optional[int]
    Performance_schema_table_handles_lost: Optional[int]
    Performance_schema_table_instances_lost: Optional[int]
    Performance_schema_thread_classes_lost: Optional[int]
    Performance_schema_thread_instances_lost: Optional[int]
    Performance_schema_users_lost: Optional[int]
    Prepared_stmt_count: Optional[int]
    Qcache_free_blocks: Optional[int]
    Qcache_free_memory: Optional[int]
    Qcache_hits: Optional[int]
    Qcache_inserts: Optional[int]
    Qcache_lowmem_prunes: Optional[int]
    Qcache_not_cached: Optional[int]
    Qcache_queries_in_cache: Optional[int]
    Qcache_total_blocks: Optional[int]
    Queries: Optional[int]
    Questions: Optional[int]
    Select_full_join: Optional[int]
    Select_full_range_join: Optional[int]
    Select_range: Optional[int]
    Select_range_check: Optional[int]
    Select_scan: Optional[int]
    Slave_heartbeat_period: Optional[Union[str, float]]
    Slave_open_temp_tables: Optional[int]
    Slave_received_heartbeats: Optional[Union[str, int]]
    Slave_retried_transactions: Optional[Union[str, int]]
    Slave_running: Optional[str]
    Slow_launch_threads: Optional[int]
    Slow_queries: Optional[int]
    Sort_merge_passes: Optional[int]
    Sort_range: Optional[int]
    Sort_rows: Optional[int]
    Sort_scan: Optional[int]
    Table_locks_immediate: Optional[int]
    Table_locks_waited: Optional[int]
    Table_open_cache_hits: Optional[int]
    Table_open_cache_misses: Optional[int]
    Table_open_cache_overflows: Optional[int]
    Tc_log_max_pages_used: Optional[int]
    Tc_log_page_size: Optional[int]
    Tc_log_page_waits: Optional[int]
    Threads_cached: Optional[int]
    Threads_connected: Optional[int]
    Threads_created: Optional[int]
    Threads_running: Optional[int]
    Uptime: Optional[int]
    Uptime_since_flush_status: Optional[int]


class ServerStatus(BaseModel):
    self_url: AnyUrl = Field(
        alias="_self",
        example="http://dbspy.example.org/status/global/mysql-server/3306",
    )
    mysql_server: str = Field(example="mysql-server:3306")
    result: GlobalStatus

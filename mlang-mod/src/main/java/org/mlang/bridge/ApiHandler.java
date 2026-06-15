package org.mlang.bridge;

import java.util.Map;

public interface ApiHandler {
    Object handle(String method, Map<String, Object> params) throws Exception;
}
